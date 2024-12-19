# Trial-Project
Application that uses a large language model to evaluate the quality of arguments presented in text

Files
1. train_model.py:
This consists of the main backend code. This loads the dataset, and then handles the user input. It also analyses the arguements, and returns the score. It uses the Flask development server, to make the app open in the browser.

2. processor.html:
This is the frontend code which styles the webpage. This is supposed to show the result of the arguement score.

3. ibmdata.csv:
This data is from the link in the spec.

Main problems I faced:
- Linking the frontend and backend codes
- I think that port 5000 was blocked by the school network, so I struggled getting the page to load.
- On running the code, you get a web link which leads to a page with a white background, so it's not working

Notes:
Since this was a little complex, I used external links to understand how everything worked. I few links I used:
1. https://stackoverflow.com/questions/73918456/from-transformers-import-berttokenizer
2. https://huggingface.co/transformers/v3.5.1/training.html
3. https://snyk.io/advisor/python/transformers/functions/transformers.BertTokenizer.from_pretrained
4. https://www.w3schools.com/tags/tag_doctype.ASP
5. https://www.geeksforgeeks.org/flask-rendering-templates/
