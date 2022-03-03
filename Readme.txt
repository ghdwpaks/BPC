이 문서는 베경화면을 코더 마음에 드는 형식으로 바꿔주기 위해서 만든 프로젝트 폴더입니다.
(2022-03-03)

간단하고 기본적인 이미지 출력만이 가능합니다.
imgs 폴더 안에 .png 형식으로만 저장된 것들이 출력 가능합니다.
다른 이미 형식은 가능한지 불가능한지 검증되지 않았습니다.

This document is a project folder created to change the screen to a codeer format.
(2022-03-03)

Only simple and basic image output is possible.
Things stored in the imgs folder in .png format can only be printed.
Other forms have not been verified whether they are possible or impossible.

오른쪽은 +
아래쪽은 +
왼쪽은 -
위쪽은 -

창 테두리 제거하는 방법 자료 : https://okky.kr/article/1052791

cv2.moveWindow('video3', x3, y3)  # Location of Drone
cv2.namedWindow('video3', cv2.WINDOW_NORMAL)  # custom size or full size
cv2.resizeWindow("video3", int(width_3), int(height_3))  # size
cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, 1)
cv2.imshow('video3', frame3)

파이썬 디렉토리 파일 리스트 가져오기 : https://itholic.github.io/python-listdir-glob/


스크린의 크기 구하기 : https://www.delftstack.com/ko/howto/python/python-get-screen-size/

from tkinter import *
root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))
mainloop()


이미지의 크기 구하기 : https://ponyozzang.tistory.com/596