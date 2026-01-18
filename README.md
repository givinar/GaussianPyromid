# GaussianPyromid
## Description
Testing Gaussian pyramid in NTBC project for improved compression

The algorithm is fed with a 512 x 512 texture as input. Next, a smoothing filter with a kernel size of 5 by 5 is applied to this texture. The result is a new smooth 256 x 256 texture. 
The new texture is interpolated to obtain the required size, and then the resulting texture is subtracted from the input (original texture). This procedure is then repeated for the resulting difference
## Results
In this example, only 2 levels were used. This means the resulting output was two 256x256 Gaussian textures and one 512x512 Laplacian texture

Original texture (512 x 512):

<img width="512" height="512" alt="Bricks085_512-PNG_Color" src="https://github.com/user-attachments/assets/7996d116-40b2-4d4e-8c95-c38fdfd9fd54" />


First iteration. Blurred image (256 x 256):

<img width="256" height="256" alt="blurred_0" src="https://github.com/user-attachments/assets/0f5dd167-b718-4501-bc21-d31c988235a3" />


Second iteration. Blurred image (256 x 256):

<img width="256" height="256" alt="blurred_1" src="https://github.com/user-attachments/assets/14ee44d3-ec56-4f6d-a911-76385d741262" />

And additional information in the form of Laplacian (512 x 512):

<img width="512" height="512" alt="laplacian" src="https://github.com/user-attachments/assets/1ba1e1c3-d064-423c-974d-9e8f1124127f" />


### Restored texture
<img width="1300" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/47551cea-7ae3-49a4-8c09-aaedb3b53023" />

