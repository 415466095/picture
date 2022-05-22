## Integrating subjective and objective picture quality scoring platform
    
This project is a comprehensive aesthetic platform, which allows people to make aesthetic evaluations on the pictures they want to evaluate, and to ensure the accuracy of their evaluations. This has the potential to be updated now that the image data is massively updated. commercial value, and provides a reliable way to describe the aesthetic preferences of contemporary populations.


The model will integrate the scores given by the neural network to the training model of the AVA dataset, supplemented by the no-reference image quality score, and finally integrate the user's subjective score for each image to give the final image aesthetic evaluation.

## Requirements

Code is written using tensorflow22 and conda 4.11.0,and Vue. Please check your config before running.

You can create the environment with when you enter the /cli1: 
```
 yarn install

```  
then you can run it with:
```
yarn run serve
```

Home page:
![image](index.png)





