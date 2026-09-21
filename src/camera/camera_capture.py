import cv2


def capture_from_camera(camera_index=0):

    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        raise RuntimeError("Camera could not be opened.")

    print("📷 EarthNex Camera")
    print("Press SPACE to capture image")
    print("Press ESC to exit")

    captured_image = None

    while True:

        success, frame = camera.read()

        if not success:
            print("Unable to read camera.")
            break

        cv2.imshow(
            "EarthNex - Terrain Camera",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        # SPACE = capture
        if key == 32:

            captured_image = frame.copy()

            cv2.imwrite(
                "captured_terrain.jpg",
                captured_image
            )

            print("✅ Terrain image captured.")
            break

        # ESC = exit
        elif key == 27:

            print("Camera closed.")
            break

    camera.release()
    cv2.destroyAllWindows()

    return captured_image


if __name__ == "__main__":

    image = capture_from_camera()

    if image is not None:
        print("📸 Image saved as captured_terrain.jpg")
