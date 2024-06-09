import os

src_name = 'videos'
src_dir = f'src\\{src_name}'

for i, video_file in enumerate(os.listdir(src_dir)):
    if os.path.isfile(os.path.join(src_dir,video_file)):
        extens_file = video_file.split(".")[-1]
        new_name = "{}{:03d}.{}".format(src_name[0], i, extens_file)
        os.rename(os.path.join(src_dir,video_file), os.path.join(src_dir,new_name))
        # print(new_name)

