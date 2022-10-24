# techsrt

Quick and dirty obsfucation script for StepMania packs (specifically for sightreading tournaments)  
  
## Usage
- Drag script into desired pack folder
- Run script
- Script will swap `#CHARTNAME` and `#TITLE` tags, remove existing `#CHARTNAME`, and obsfucate preview music/song artist

Also requires a silent.ogg file present in a different folder within the pack to properly obsfucate preview music (default name `resources`, can change to whatever)

Requires Ash's [simfile library](https://github.com/garcia/simfile) for Python
