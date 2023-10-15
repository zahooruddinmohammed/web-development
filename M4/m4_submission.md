<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Zahooruddin Zohaib Mohammed (zm254)</td></tr>
<tr><td> <em>Generated: </em> 10/15/2023 7:16:13 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/zm254" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.18.10image.png.webp?alt=media&token=57572ecc-6d18-47a4-bceb-7d08f8988f4e"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation of float<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.18.56image.png.webp?alt=media&token=9990a2b2-3612-42ad-ac2f-3e6200b68bd2"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation of int<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.19.25image.png.webp?alt=media&token=61541886-5ca1-4054-b435-d524506f04c2"/></td></tr>
<tr><td> <em>Caption:</em> <p>converting strings into proper datatype<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.20.03image.png.webp?alt=media&token=1ec22ea4-867f-4e50-a1db-6944aac31dfa"/></td></tr>
<tr><td> <em>Caption:</em> <p>add function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.20.56image.png.webp?alt=media&token=90956dc4-7836-45c0-91ac-9371e20a76a7"/></td></tr>
<tr><td> <em>Caption:</em> <p>subtraction function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.21.29image.png.webp?alt=media&token=02109e95-ca76-4759-b7c3-da8e923b1fd3"/></td></tr>
<tr><td> <em>Caption:</em> <p>mult function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.22.36image.png.webp?alt=media&token=b516fec3-6090-45ee-a9ef-ebf799fc0868"/></td></tr>
<tr><td> <em>Caption:</em> <p>div function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.23.06image.png.webp?alt=media&token=be5bd871-f5f1-4902-b9ed-d056c31edbce"/></td></tr>
<tr><td> <em>Caption:</em> <p>main logic part1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.24.10image.png.webp?alt=media&token=d636819b-d3ff-401f-920a-02c61aa9fb56"/></td></tr>
<tr><td> <em>Caption:</em> <p>main logic part2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.25.38image.png.webp?alt=media&token=1e390175-e469-4d99-b155-7e42ed54d2b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>main logic part3<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.50.34image.png.webp?alt=media&token=81649d67-e6a5-400f-a518-f24545d7b5d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>number add number test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.52.50image.png.webp?alt=media&token=b7e6e1b6-26a2-4669-8c88-5b2cf20a495e"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans add number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.53.48image.png.webp?alt=media&token=dd841a52-2a1e-45c2-b17e-d999ad19644d"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-sub-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.55.10image.png.webp?alt=media&token=0f8723a5-33db-42b2-bee8-9b0d7079302f"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-sub-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.56.56image.png.webp?alt=media&token=0a7a30b4-78f6-4179-91f7-4c518fd2dcec"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.58.07image.png.webp?alt=media&token=6e3d556e-8d96-4acd-80ed-d7d9b6da2309"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-mult-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.58.59image.png.webp?alt=media&token=cca7fdf6-3e49-448f-90e9-06357041567e"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fzm254%2F2023-10-15T22.59.40image.png.webp?alt=media&token=7ab596fd-a648-474b-a7b4-9c44dffe4a55"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>i learned about pytest configuring in the start was a little problem and<br>later as i got help through online through notes i figureed and leart<br>it the best way to implement the testcases. And also using split() split<br>the string and then use ans from the previos function to get the<br>ans<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 14px;">Test cases provide a way to verify&nbsp;</span>that the software is working<br>as intended and meets the specified requirements. In the context of Pytest, test<br>cases are defined as functions that use assertions to verify the behavior of<br>the code being tested.</div><div><span style="font-size: 14px;">Pytest makes it easy to define&nbsp;</span>and organize test<br>cases, with a simple syntax and flexible framework that allows&nbsp;tests to be written<br>in a clear and concise way. Pytest also supports a wide range of<br>testing scenarios, from simple unit tests to more complex integration and end-to-end tests.<br>During this assignment, I learnt some new techniques for organizing and structuring test<br>cases in Pytest. For example, I learned about the use of fixtures to<br>manage the setup and tear-down of test environments, which can help to reduce<br>duplication and improve the maintainability of test cases. I also learned about the<br>use of parametrized tests, which allow multiple inputs to be tested using a<br>single test case. This can be a useful technique for testing functions or<br>methods that have multiple possible inputs, and can help to reduce the amount<br>of code needed to write and maintain tests.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/zahooruddinmohammed/zm254-is601-007/pull/11">https://github.com/zahooruddinmohammed/zm254-is601-007/pull/11</a> </td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/zm254" target="_blank">Grading</a></td></tr></table>