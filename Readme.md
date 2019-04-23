# Software demo for IST597

## User manual and interface

1. The website is currently available at [http://34.83.40.8:8080](http://34.83.40.8:8080/)

2. The brief overview for the states of art are shown in the first page

3. Click application and you can transform your own image by SRCNN and EDSR.

4. You may need to clear cache in chromes to see the result after waiting.

## Source code implement algorithms

Codes are included in the algorithms. <https://github.com/ymlwww/ist597final>

Code reference: 

1. https://github.com/thstkdgus35/EDSR-PyTorch

2. <https://github.com/icpm/super-resolution>

## Performance evaluation

As for the web application, the performance is relatively stable. Sometimes there is a delayed show and you may need to reupload the file or refresh the page. Images whose size is as small as 15KB are suggested since the testing of networks takes time.

1. Contribution
   1. Implement five commons frameworks for image super resolution
   2. Deploy the website for image super resolution
   
2. Limitation 
  
   1. Employ the deformable CNN for EDSR but the loss never converge.
   
   2. The EDSR with DCNN is easy to break down on the K80 machine.
   
   3. The training and testing is relatively slow especially for biomedical images.
   
3. Potential Development

   1. Cut down the dimentsion of DCNN to help converge.
   2. Pretain DCNN on imagenet and then replace the specific CNN layer in EDSR

Futher numerical results will be included inthe presentation.

