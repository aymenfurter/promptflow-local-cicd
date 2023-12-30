# Integrate PromptFlow into Your CI/CD pipeline (On-Agent)

## Overview
> [!Note]
> This sample demonstrates adding PromptFlow evaluations in existing Python applications, including LangChain and others like Semantic Kernel's Python version. At present, it directly runs PromptFlow on the agent. It's ideal for smaller applications with an established deployment setup, looking to use PromptFlow solely for evaluation purposes. If you are looking for an end-to-end solution using PromptFlow, I recommend exploring the [LLMOps template repository on GitHub.](https://github.com/microsoft/llmops-promptflow-template/)

Every AI app should include evals! With [PromptFlow](https://microsoft.github.io/promptflow/), we ensure not only the functional correctness of our code but also the precision and reliability of AI inferences, preventing issues like hallucinations. For more information about PromptFlow, visit the [PromptFlow documentation](https://microsoft.github.io/promptflow/) and the [GitHub repository](https://github.com/microsoft/promptflow). 


## Getting Started with this Sample 🛠️

### Setting Up Azure Pipelines

To set up Azure Pipelines for this project:

1. **Create a Variable Group:** 
   - The pipeline depends on a specific variable group named `promptflow-evals`. 
   - Ensure this group includes all necessary variables, such as `DEPLOYMENT_NAME`, `AZURE_OPENAI_ENDPOINT`, and `AZURE_OPENAI_API_KEY`.

2. **Configure the Pipeline:**
   - Modify the `azure-pipelines.yaml` file according to your project's needs. 
   - This file outlines the build and test processes, integral to integrating PromptFlow evaluations into your CI/CD workflow.

3. **Run the Pipeline:**
   - Trigger the pipeline through Azure Pipelines.
   - Upon completion, the results of the PromptFlow evaluations will be accessible as an artifact.
   - Review this artifact for a detailed report of the evaluations.

### Using VS Code Extension for PromptFlow

VS Code, complemented by the PromptFlow extension, offers an intuitive environment for working with PromptFlow:

1. **Install Required Tools:**
   - Download and install the latest stable version of [VS Code](https://code.visualstudio.com/).
   - Add the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
   - Install the [PromptFlow extension for VS Code](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow).

2. **Set Up Your Environment:**
   - Choose the appropriate Python interpreter in VS Code.
   - Use the visual editor to open `flow.dag.yaml` for an enhanced flow editing and testing experience.
