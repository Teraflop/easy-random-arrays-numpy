<h1>Easy Random Arrays With Numpy</h1>

<p> This is my first project I'm putting on Github, so it's more or less
just a test of releasing a project. I'm sure much of my linear algebra
terminology is wrong, and that this program is not the most elegant way to
generate random numpy arrays with whole numbers. Still, I hope that you find
this handy for generating random arrays to work with that aren't decimals. </p>

<h3> Usage </h3>
<p>To use this code, just clone the repository or copy the code into a .py file.
Then, import the file and use its functions in your own code.</p>

<h5>Example</h5>
'''python
<p> import numpyArrayCreation as nac </p>
<p> foo = nac.createNormalMatrix(5, 5, 2)
</p>
'''

<h3>Requirements</h3>
<p>Python 3</p>
<p>Numpy</p>

<h3>Functions</h3>
<p> This project is consisted of four functions: createMatrix, create1DArray,
createNormalMatrix, and createNormal1DArray.</p><p> The createMatrix() function takes
3 parameters: width, height, and magnitude. The width parameter specifies
the number of columns in the matrix, the height parameter specifies the number
of rows in the matrix, and the magnitude parameter specifies the range
of numbers in the array. A value of 1 will provide numbers from 1 to 10, 2 will
provide 1-100, and so on. createNormalMatrix() takes the same parameters, the only difference is that they will be (kind of) normally distributed. The way the rounding
works might throw that off. It yields both positive numbers and negative numbers, while createMatrix() yileds only positive or negative numbers, depending on if the magnitude value is positive or negative. </p>

<p>The create1DArray() function takes two parameters: size and magnitude. The
size parameter indicates how many numbers are in the vector, and the magnitude parameter specifies the range
of numbers in the array. A value of 1 will provide numbers from 1 to 10, 2 will
provide 1-100, and so on. createNormal1DArray()  works similarly; the only difference is that they will be (kind of) normally distributed. The way the rounding
works might throw that off. It yields both positive numbers and negative numbers, while create1DArray() yileds only positive or negative numbers, depending on if the magnitude value is positive or negative.</p>

<p>If any invalid numbers or non integers are entered as parameters, all of the functions will return None.</p>
