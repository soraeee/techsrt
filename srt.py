''' 
huge thank you to ash for making this script functional 
'''

import os
import simfile
from simfile.ssc import SSCSimfile
from simfile.types import Chart

def anonymize(path: str):
	print(f"Anonymizing {path}")
	with simfile.mutate(path) as sim:
		for chart_ in sim.charts:
			chart: Chart = chart_ # typing workaround
			
			# Change title to chartname and clear chartname afterwards
			if "CHARTNAME" in chart:
				newTitle = chart.chartname
				sim.title = newTitle
				chart.chartname = ""

		# Obfuscate other aspects of the simfile 
		sim.titletranslit = ""
		sim.artisttranslit = ""
		sim.artist = "Unknown artist"
		sim.preview = "../Resources/silent.ogg"
		sim.subtitle = ""
		sim.samplestart = "0.000"
		sim.samplelength = "10.000"
		sim.background = "../bg.png"
		sim.banner = "../bn.png"

# Remove .sm, .old, .auto files
def wipesm(path: str):
	for item in os.listdir(path):
		ext = [".sm", ".old", ".auto"]
		for i in range(len(ext)):
			if item.endswith(ext[i]):
				print(f"Cleaning {ext[i]} of {path}")
				os.remove(os.path.join(path, item))

def main():
	path = os.getcwd()
	for simfileDir in simfile.dir.SimfilePack(path).simfile_dirs():
		if simfileDir.ssc_path:
			anonymize(simfileDir.ssc_path)
			# Don't wipe .sm files if there is no .ssc file, just in case
			wipesm(simfileDir.simfile_dir)

if __name__ == "__main__":
	main() 