**Prompt**
- A prompt is an question, instruction, context  that we give to a llm to guide its reponse.
- In simple language prompt is how we communicate with llm model 


**Component of Prompts**
- There are 5 major component if any good prompt 
    - Role  
    - Context
    - Instruction / Tasks 
    -  Input 
    - Constrain 
    - output 

**A well-designed prompt reduces ambiguity and gives the model useful context**

Eg : 

```
### Role
You are a Senior AWS Solution Architect with extensive experience in AWS cloud architecture, security, hosting, deployment, and cost optimization.

### Context
You advise customers on AWS infrastructure, security best practices, deployment strategies, and cost-effective architecture.

### Task
Answer the user's AWS-related question with technically accurate, actionable recommendations aligned with AWS best practices.

### User Question
How can I ensure that files stored in my Amazon S3 bucket are not publicly accessible?

### Constraints
- Keep the response under 300 words.
- Be concise, specific, and actionable.
- Prioritize AWS security best practices.
- Do not invent AWS features, settings, or documentation references.
- If you do not know the answer, respond exactly: "I don't know."
- Reference official AWS documentation wherever possible.

### Output Format
**Answer:**  
[Provide a direct answer to the question.]

**Reference:**  
[Provide relevant official AWS documentation links.]

**Steps to be taken on AWS:**  
[Provide numbered, actionable steps using the AWS Management Console.]
    
```

**Prompt Template**
-  A prompt template is reuseable strucher for creating prompt dynamically by inserting different value into placeholder 

- Let's say if we are builing a story teller genai app and we need thousands of customer to user our story telling app or learning app we don't want to create custom mutiple prompt we need a dynamic way to handle all type of request from user

Eg :  In Story teller app
    - Motivational 
    - love 
    - Fighting
    - life messages 
    - kids story 

Learning App :
    - Coocking 
    - Gardening 
    - Science / Maths / Physics etc 

Hence we need prompt template to reuse the prompt with dofferent conetxt which we can give using placeholder.

- prompt template is a class in langchain whcih we can import
    ``` from lanchain.prompts import prompTeamplate ```

Important :  prompt template is majorly used to create simple web application where we want a simple user query to be resposnded with a model answer.

