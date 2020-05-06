import pytube
import os
import subprocess
YouTube_Url='empty'
while YouTube_Url !='':
    YouTube_Url=input("추출하실 주소를 입력하세요/종료를 원하시면 입력하시마세요")
    if YouTube_Url !='':
        yt = pytube.YouTube(YouTube_Url)
        videos=yt.streams.all()
        for index,i in enumerate(videos):
            print(index,'.',i,sep='')
        cNum=int(input("다운 받을 화질은 입력하세요.(0~21)"))
        down_dir='C:/youtube'
        videos[cNum].download(down_dir)
        OriFileName=videos[cNum].default_filename
        subprocess.call(['ffmpeg','-i',
        os.path.join(down_dir,OriFileName),
        os.path.join(down_dir,OriFileName.replace('.mp4','.mp3'))])
        print('완료')
