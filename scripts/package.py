import os
import shutil
import zipfile

def copy_and_zip_folders(source_dir, folders_to_include, output_zip):
	# Create a temporary directory to copy the target folders
	temp_dir = os.path.join(os.path.dirname(output_zip), 'temp')
	os.makedirs(temp_dir, exist_ok=True)

	try:
		# Copy the specified folders to the temporary directory
		for folder in folders_to_include:
			folder_path = os.path.join(source_dir, folder)
			target_path = os.path.join(temp_dir, folder)
			shutil.copytree(folder_path, target_path)

		# Copy pack.mcmeta to the temporary directory
		pack_mcmeta_path = os.path.join(source_dir, 'pack.mcmeta')
		shutil.copy2(pack_mcmeta_path, temp_dir)

		# Copy pack.png to the temporary directory
		pack_png_path = os.path.join(source_dir, 'pack.png')
		shutil.copy2(pack_png_path, temp_dir)

		# Create a ZIP archive of the copied folders and file
		with zipfile.ZipFile(output_zip, 'w') as zipf:
			for folder in folders_to_include:
				folder_path = os.path.join(temp_dir, folder)
				for root, files in os.walk(folder_path):
					for file in files:
						file_path = os.path.join(root, file)
						arcname = os.path.relpath(file_path, temp_dir)
						zipf.write(file_path, arcname=arcname)

			# Add pack.mcmeta to the ZIP archive
			zipf.write(pack_mcmeta_path, arcname=os.path.basename(pack_mcmeta_path))

	finally:
		# Clean up temporary directory
		shutil.rmtree(temp_dir)
		print('\n' + ('#' * 20) + '\nAll operations complete. You can now safely close this file.\n' + ('#' * 20))

# Settings
version = '2.5'
source_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
folders_to_include = ['assets']
output_zip_file = 'scripts/bin/ssbrc_' + version + '.zip'

copy_and_zip_folders(source_directory, folders_to_include, output_zip_file)
