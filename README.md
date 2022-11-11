# techsrt

Quick and dirty obsfucation script for StepMania packs (specifically for sightreading tournaments)  
  
## Usage
- Drag script into desired pack folder
- Run script
- Script will swap `#CHARTNAME` and `#TITLE` tags, remove existing `#CHARTNAME`, obsfucate preview music/song artist, set graphics as appropriate, and move all files into appropriate group folders

Also requires:
- a silent.ogg file present in a different folder within the pack to properly obsfucate preview music (default name `Resources`, can change to whatever)
- appropriately named graphics in the Resources folder (todo: make this more flexible)
- Filled out obscured chartnames in all .ssc files, and chartnames/group + tier data in the srtFiles list
- Funny subtitles for tiers, i guess? (todo also make this flexible, or just make everything flexible at once lol)

Requires Ash's [simfile library](https://github.com/garcia/simfile) for Python
