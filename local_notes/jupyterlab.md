**Table of Contents**

[TOC]

# Introduction to JupyterLab
---

[Jupyter](https://jupyter.org/) and offers a flexible and powerful toolkit for working with projects involving Jupyter notebooks, code, and data. This guide will cover all the essentials to get you started with JupyterLab, including detailed steps and examples.

## What is JupyterLab?
---

JupyterLab is an integrated development environment (IDE) that provides a flexible and scalable interface for the Jupyter Notebook system. It supports interactive data science and scientific computing across over 40 programming languages (including Python, Julia, and R).

**Key features:**

- Code, compile, and run in multiple languages.
- A modular interface with customizable layout.
- Integration with Git and other version control systems.
- Supports real-time collaboration.

# Starting JupyterLab
---

On the bwVisu nav-bar click `Interactive Apps` --> `JupyterLab`. Than specify the resources and click `Launch`. This will open JupyterLab in your current web browser.

## The JupyterLab Interface
---

**Left Sidebar:**
:    Contains file browser, running kernels, command palette, and extensions.

**Main Workspace:**
:    Area where notebooks and files are displayed.

**Top Menu:**
:     Provides access to file, edit, view, and run commands.

# Working with Notebooks
---

You can create a new notebook via the `+` button in the file browser or the `File` menu. Enter your code in a cell, and press ++shift+enter++ to execute the code in that cell. Every cell accepts valid code and module imports. Example Python code:

```{.python linenums="1" title="Python"}
from matplotlib import pyplot as plt
import numpy as np

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()
```

Markdown cells allow you to add formatted text to explain your code, using Markdown syntax.

**Advanced Features:**

- JupyterLab supports numerous extensions that enhance functionality, such as the JupyterLab Git extension.
- Interactive IPython widgets can enhance notebook interactivity.

# Tips and Tricks
---

- Learn and use keyboard shortcuts to improve productivity in JupyterLab.
- Customize the layout by dragging and resizing panels.

## Advanced Mathematical Operations
---

JupyterLab supports LaTeX for advanced mathematical operations. For example, to display a complex mathematical equation:

```{.LaTeX linenums="1" title="LaTeX"}
\begin{equation}
f(x)  = \int_{-\infty}^\infty
    f\hat\xi\,e^{2 \pi i \xi x}
    \,d\xi
\end{equation}
```

**Which outputs:**

\begin{equation}
f(x)  = \int_{-\infty}^\infty
    f\hat\xi\,e^{2 \pi i \xi x}
    \,d\xi
\end{equation}

## Add packages via virtual environments
---

1. Open a terminal and type:
    ```bash
    python3 -m venv <myEnv>
    ```
2. Activate your environment: 
    ```bash
    source <myEnv>/bin/activate
    ```
3. Install your packages:  
    ```bash
    pip install -U pip
    pip install <mypackage>
    ```
4. Install the ipykernel package: 
    ```bash
    pip install ipykernel
    ```
5. Register your virtual environment as custom kernel to Jupyter:
    ```bash
    python3 -m ipykernel install --user --name=<myKernel>
    ```

## Add packages via miniconda
---

1. Load the miniconda module by clicking first on the blue hexagon icon on the left-hand side of Jupyter's start page and then on the "load" Button right of the entry for miniconda in the software module menu.
2. Open a terminal and type:   
    ```bash
    conda create --name <myenv>
    ```
3. Activate your environment:   
    ```bash
    conda activate <myenv>
    ```
4. Install your packages:   
    ```bash
    conda install <mypackage>
    ```
5. Install the ipykernel package:  
    ```bash
    conda install ipykernel
    ```
6. Register your virtual environment as custom kernel to Jupyter:   
    ```bash
    python3 -m ipykernel install --user --name=<myKernel>
    ```

## How to update the python version
---

1. Activate the Miniconda.
2. Create a virtual environment with a custom python version via conda:
    ```bash
    conda create --name <myenv> python=<python version>
    ```
3. Install the ipykernel package:
    ```bash
    conda install ipykernel
    ```
4. Register your virtual environment as custom kernel to Jupyter:  
    ```bash
    python3 -m ipykernel install --user --name=<myKernel>
    ```
5. Select your newly created kernel in Jupyter

## Multi-Language Support
---

JupyterLab supports over 40 programming languages including Python, R, Julia, and Scala. This is achieved through the use of different kernels, which are implementations of the Jupyter notebook environment for each language. You can switch between kernels easily, allowing you to use the best tool for a specific task.

Example of switching kernels in a notebook:

1. On the cluster:
    ```
    $ module load math/R
    $ R
    > install.packages('IRkernel')
    ```
2. On bwVisu:
    1. Start Jupyter App
    2. In left menu: load math/R
    3. Open Console:
    ```
    $ R
    > IRkernel::installspec(displayname = 'R 4.2')
    ```
    4. Start kernel 'R 4.2' as console or notebook

# Real-Time Collaboration
---

JupyterLab supports real-time collaboration features, allowing multiple users to edit documents simultaneously. This feature is similar to collaborative editing in Google Docs but is designed for code, notebooks, and data. This is particularly useful for teams working on data analysis, machine learning models, or scientific research.

# Interactive Widgets
---

JupyterLab supports interactive widgets that can create UI controls for interactive data visualization and manipulation within the notebooks. Example of using an interactive widget:

```{.python linenums="1" title="Python"}
from ipywidgets import IntSlider
slider = IntSlider()
display(slider)
```

These widgets can be sliders, dropdowns, buttons, etc., which can be connected to Python code running in the backend.
