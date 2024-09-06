import librosa
import numpy as np
import os
import matplotlib.pyplot as plt
INPUT = "0001_000351.wav"

def convert(wave, spec_folder):
    #Create correct Spectrogram name:
    name, _ = os.path.splitext(os.path.basename(wave))
    extension = '.png'
    new_name = os.path.join(spec_folder, name + extension)
    #Load Sound File
    y, sr = librosa.load(wave)

    #Convert to Spectrogram
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    spectrogram_db = librosa.amplitude_to_db(spectrogram, ref=np.max)
    plt.figure(figsize=(6,4))
    librosa.display.specshow(spectrogram_db, sr=sr, x_axis='time', y_axis='mel', cmap='coolwarm', fmax=8000)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(new_name, bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()


#Set up corpus location
root = os.getcwd()
destination = os.path.join(root, "Spectrograms")
all_directories = []

#Convert corpus from wave files to .png image files
for path, folders, files in os.walk(root):
    for file in files:
        dest = os.path.join(path, "Spectrograms")
        full_file_path = os.path.join(path, file)
        if os.path.exists(dest):
            if file.endswith('.wav'):
                convert(full_file_path, dest)
        else:
            os.mkdir(dest)
            if file.endswith('.wav'):
                convert(full_file_path, dest)
            