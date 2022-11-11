''' 
huge thank you to ash for making this script functional 

future improvements todo list:
- remove extra difficulties (i think i did this but i don't know if it works)
- figure out why the CHARTNAME assert breaks on metallic punisher???
- script-wide variables for more flexibility
'''

import os
import shutil
import simfile
from simfile.ssc import SSCSimfile
from simfile.types import Chart, Charts, Simfile

''' 
HOW TO FILL OUT srtFiles:
- have a google sheets
- copy your funny chartname columns into a text editor
- use multiline editing idk good luck (it's still faster than manually processing 50 damn files though)
'''

# obscured chartname, tier, group
# group -1 is reserved for quali/extras
srtFiles = [
	# example chart: ["Funny Chartname", 2, 3]
]

# tier subtitle, number of groups per tier
tierNames = [
	# example tier: ["Funny Subtitle," 4]

]

def anonymize(path: str):
	print(f"Anonymizing {path}")
	with simfile.mutate(path) as sim:
		for chart_ in sim.charts:
			chart: Chart = chart_ # typing workaround

			# Remove all non-expert difficulties
			if chart and chart.stepstype == 'dance-single' and chart.difficulty == 'Challenge':
				sim.charts = [chart] # this might break horribly
			
			# Change title to chartname and clear chartname afterwards
			#assert "CHARTNAME" in chart, f"File {sim.title} does not have a CHARTNAME" # this assert breaks on one mirin file for some reason???
			if "CHARTNAME" in chart and chart.difficulty == 'Challenge': # god
				newTitle = chart.chartname
				sim.title = newTitle
				chart.chartname = ""

		# Obfuscate other aspects of the simfile 
		sim.titletranslit = ""
		sim.artisttranslit = ""
		sim.artist = "???"
		sim.preview = "../Resources/silent.ogg"
		sim.subtitle = ""
		sim.samplestart = "0.000"
		sim.samplelength = "10.000"
		#sim.background = "../Resources/bg.png"
		#sim.banner = "../bn.png"

# Remove .sm, .old, .auto files
def wipesm(path: str):
	for item in os.listdir(path):
		ext = [".sm", ".old", ".auto"]
		for i in range(len(ext)):
			if item.endswith(ext[i]):
				print(f"Cleaning {ext[i]} of {path}")
				os.remove(os.path.join(path, item))

# Create folders
def createFolders():
	print("Creating folders...")
	root = os.getcwd()
	for i in range(len(tierNames)):
		for j in range(tierNames[i][1]):
			# Make a folder with appropriate naming
			newpath = os.path.join(root, "TPE Tier " + str(i + 1) + " - " + tierNames[i][0] + " (Group " + str(j + 1) + ")")
			os.mkdir(newpath)

			# Copy simfile resources over (silent, bg, appropriate banner)
			os.mkdir(os.path.join(newpath, "Resources"))
			shutil.copyfile(os.path.join(root, "Resources/silent.ogg"), os.path.join(newpath, "Resources/silent.ogg"))
			shutil.copyfile(os.path.join(root, "Resources/tpe bg.png"), os.path.join(newpath, "Resources/tpe bg.png"))
			shutil.copyfile(os.path.join(root, "Resources/tpe bn t" + str(i + 1) + ".png"), os.path.join(newpath, "bn.png"))
	
	# Create extra/qualifier folders on their own
	qualipath = os.path.join(root, "TPE - Qualifier")
	os.mkdir(qualipath)
	os.mkdir(os.path.join(qualipath, "Resources"))
	shutil.copyfile(os.path.join(root, "Resources/silent.ogg"), os.path.join(qualipath, "Resources/silent.ogg"))
	shutil.copyfile(os.path.join(root, "Resources/tpe bg.png"), os.path.join(qualipath, "Resources/tpe bg.png"))
	shutil.copyfile(os.path.join(root, "Resources/tpe bn quali.png"), os.path.join(qualipath, "bn.png"))

	expath = os.path.join(root, "TPE - Extras")
	os.mkdir(expath)
	os.mkdir(os.path.join(expath, "Resources"))
	shutil.copyfile(os.path.join(root, "Resources/silent.ogg"), os.path.join(expath, "Resources/silent.ogg"))
	shutil.copyfile(os.path.join(root, "Resources/tpe bg.png"), os.path.join(expath, "Resources/tpe bg.png"))
	shutil.copyfile(os.path.join(root, "Resources/tpe bn extra.png"), os.path.join(expath, "bn.png"))
	print("Folders created.")

# Move files into group folders
# path should be the folder of the simfile
def createSRT(path: str):
	root = os.getcwd()
	toPath = ""
	fromPath = ""
	if path.ssc_path:
		with simfile.mutate(path.ssc_path) as sim:
			print(f"Moving {path.simfile_dir}")

			# This is going off of obscufated titles - intended to be ran after anonymize()
			# index() is a binch and won't work properly with multidim arrays fuck you
			ind = -1
			for i in range(len(srtFiles)):
				if srtFiles[i][0].lower().strip() == sim.title.lower().strip(): # FUCK
					ind = i
					print(f"Found file, ind = {ind}")
					
			assert ind >= 0, f"Title {sim.title} not found in srtFiles list"

			# Set appropriate metadata and find the folder to move to
			sim.background = "../Resources/tpe bg.png"
			sim.banner = "../bn.png"
			
			if srtFiles[ind][1] == 7: # qualifier
				toPath = os.path.join(root, "TPE - Qualifier")

			elif srtFiles[ind][1] == 6: # extras
				toPath = os.path.join(root, "TPE - Extras")

			else: # regular files
				toPath = os.path.join(root, "TPE Tier " + str(srtFiles[ind][1]) + " - " + tierNames[srtFiles[ind][1] - 1][0] + " (Group " + str(srtFiles[ind][2]) + ")")
			
			fromPath = path.simfile_dir

	for subdir, dirs, files in os.walk(root):
		if subdir == toPath:
			shutil.move(fromPath, toPath)



def main():
	path = os.getcwd()
	createFolders()
	for simfileDir in simfile.dir.SimfilePack(path).simfile_dirs():
		if simfileDir.ssc_path:
			anonymize(simfileDir.ssc_path)
			# Don't wipe .sm files if there is no .ssc file, just in case
			wipesm(simfileDir.simfile_dir)
	
	for simfileDir in simfile.dir.SimfilePack(path).simfile_dirs():
		createSRT(simfileDir) ## do this after because idk lmfao, i can't be bothered to check if it works in the other loop

if __name__ == "__main__":
	main() 