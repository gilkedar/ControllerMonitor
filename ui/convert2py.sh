UI_FILES_PATH="/home/$USER/workspace/ControllerMonitor/ui/ui_files/"

for filename in $UI_FILES_PATH*.ui ; do
  base_name="$(basename -- "$filename")"
  target_path="$UI_FILES_PATH${base_name%%.*}.py"
  echo "converting $filename -> $target_path";
  pyuic5 -x $filename -o $target_path;
done


echo "done converting ui files to python!"
