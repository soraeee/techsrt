# techsrt

Quick and dirty obsfucation script for StepMania packs (specifically for sightreading tournaments)  
  
## Usage
- Drag script into desired pack folder
- Run script
- Script will swap `#CHARTNAME` and `#TITLE` tags, remove existing `#CHARTNAME`, and obsfucate preview music/song artist

Also requires:
- a silent.ogg file present in a different folder within the pack to properly obsfucate preview music (default name `Resources`, can change to whatever)
- appropriately named graphics in the Resources folder (todo: make this more flexible)
- Filled out obscured chartnames in all .ssc files, and chartnames/group + tier data in the srtFiles list
- Funny subtitles for tiers, i guess? (todo also make this flexible, or just make everything flexible at once lol)

Requires Ash's [simfile library](https://github.com/garcia/simfile) for Python
