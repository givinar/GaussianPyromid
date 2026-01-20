# Description of the experiment

The original texture, the texture after smoothing (Gaussian) and the Laplacian were analyzed. The analysis implies obtaining statistical characteristics, as well as constructing a frequency distribution of pixels

The experiment was conducted with only one level of decomposition, that is, only one Gaussian texture and only one Laplacian are required to reconstruct the image

## Results
### Statistical characteristics
Statistical characteristics of textures include the analysis of each channel separately, as well as the analysis of the gray image

| Type | Image | R channel | G channel | B channel | Common stats<br/>(in grayscale) |
|---|---|---|---|---|---|
| Origin image<br/>(512x512) | <img width="128" height="128" alt="Bricks085_512-PNG_Color" src="https://github.com/user-attachments/assets/bd82a8f3-38af-422b-a69f-7fcfaed810ce" /> | Mean: 149.35<br/> Variance: 495.53<br/> std: 22.26<br/> Range: 40 - 232 | Mean: 116.94<br/> Variance: 1252.56<br/>std: 35.39<br/>Range: 44 - 232 |Mean: 99.15<br/>Variance: 1169.55<br/>std: 34.20<br/>Range: 37 - 233|Mean: 124.60<br/>Variance: 938.12|
| Blurred image<br/>(256x256) | <img width="64" height="64" alt="blurred_0" src="https://github.com/user-attachments/assets/54a0d0eb-0868-4217-b0d0-3f933cba3bf8" /> |Mean: 149.34<br/>Variance: 393.28<br/>std: 19.83<br/>Range: 62 - 201|Mean: 116.93<br/>Variance: 1063.87<br/>std: 32.62<br/>Range: 60 - 194|Mean: 99.13<br/>Variance: 998.51<br/>std: 31.60<br/>Range: 54 - 185|Mean: 124.59<br/>Variance: 788.07|
| Laplacian image<br/>(512x512) | <img width="128" height="128" alt="laplacian" src="https://github.com/user-attachments/assets/e8cf8202-5150-48be-8294-ea645c66adc4" /> |Mean: 108.59<br/>Variance: 14609.22<br/>std: 120.87<br/>Range: 0 - 255|Mean: 115.55<br/>Variance: 14622.05<br/>std: 120.92<br/>Range: 0 - 255|Mean: 119.21<br/>Variance: 14779.35<br/>std: 121.57<br/>Range: 0 - 255|Mean: 113.89<br/>Variance: 12279.17|

### Histograms

#### Original image
<img width="1920" height="975" alt="orig_hist" src="https://github.com/user-attachments/assets/f32ad6e3-5ae0-4f9f-a8ac-19803003f52f" />

#### Blurred image
<img width="1920" height="975" alt="blur0" src="https://github.com/user-attachments/assets/16c192d5-beab-4231-9ff4-e35c5e318efa" />

#### Laplacian image
<img width="1920" height="975" alt="lap" src="https://github.com/user-attachments/assets/f5de4206-491b-449f-ab03-796b50d5f47c" />

## Conclusions
The texture obtained after applying a Gaussian filter has a histogram similar to the original image. 
This texture concentrates the main information contained in the original, but its main advantage is that the resulting texture is half the size of the original for each dimension. 
Therefore, baking the resulting texture requires a hash grid that is four times smaller than the original.

Furthermore, statistical analysis of the Laplacian shows a large standard deviation and a wide range of values, but the histogram shows that a narrow band of pixel values ​​is required to preserve the Laplacian. 
Although the Laplacian size is identical to the original image, this narrow band allows for the use of much fewer bits (quantization) to store information without loss of precision.

In my opinion, we can get good compression with pre-processing of the image using the current algorithm.
