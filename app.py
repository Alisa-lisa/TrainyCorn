from typing import Optional
import cv2
import mediapipe as mp
import typer

app = typer.Typer()

@app.command()
def start_camera(save: bool = True, output_name: Optional[str] = None):
    resources = []
    # Open the camera
    try:
        cap = cv2.VideoCapture(0)
        resources.append(cap)
        # Define the codec and create VideoWriter object
        if save:
            output: str = f"{output_name}.avi" if output_name is not None else "output.avi"
            fourcc = cv2.VideoWriter_fourcc(*'MP4V')
            out = cv2.VideoWriter(output, fourcc, 20.0, (640,  480))
            resources.append(out)
        while cap.isOpened():
            ret, frame = cap.read()  # frame by frame reading
            """ Placeholder for the operations """
            if save:
                # frame = cv2.flip(frame, 0)
                out.write(frame)

            cv2.imshow('Pose detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        for i in resources:
            i.release()
        cv2.destroyAllWindows()
    except Exception as ex:
        print(f"Could not use camera due to {ex}")


if __name__ == "__main__":
    app()
