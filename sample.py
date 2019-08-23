# OpenCV のインポート
import cv2

# VideoCaptureのインスタンスを作成する。
# カメラ選択
cap = cv2.VideoCapture(0)

while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

   # 加工なし画像を表示する
    cv2.imshow('Main Frame', frame)
    #原画は残す。以降の画像処理はeditframeに対して行う
                       
    editframe = frame
    # 以降の画像処理は、frameに対して行います

    #----------------------以下に処理を追加-------------------------------------

    #画像検査（結果検出）のおおまかな流れ
    #①画像入力
    #
    #②画像加工（前処理）
    #検査を容易に行うための画像を加工
    #ノイズの除去や色の選別、濃淡の強調などを行う。
    #画像検査は前処理が肝
    #
    #③二値化
    #ラベリング処理に必要な画像を作成
    #OpenCVでは二値化画像でないとラベリングできない
    #
    #④ラベリング（欠陥検出）
    #
    
    # Samle処理　消していただいて構いません                   
    # 文字列を表示
    cv2.putText(editframe, 'PPE_Internship ', (0,25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255,255), 2, cv2.LINE_AA)





    # 加工済の画像を表示する
    cv2.imshow('Edit Frame', editframe)


    #----------------------処理以上---------------------------------------------
    # ESCキーで終了
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
