**Table of Contents**

[TOC]

# Introduction to RStudio
---

[RStudio](https://posit.co/download/rstudio-server/) is an IDE that supports the development and execution of R, a programming language for statistical computing and graphics. It enhances R's user experience by providing an organized workspace with tools for plotting, history, debugging, and workspace management. RStudio primarily supports the R programming language. However, it does provide integrated support for several other languages through various means, especially in the context of R Markdown documents and Shiny applications. 

## Key features
---

- Integrated R help and documentation.
- Tools for plotting, history, debugging, and managing your workspace.
- Supports Markdown, Shiny, and HTML.
- Extensive package management.

## Starting RStudio
---

Before starting RStudio, you can install/load R. If you want to use a specific version of R you can load a module or use a custom version from your home directory. For a custom R-version make sure you add it to the `PATH` and check that it is the default version by checking `R --version`. But this is just optionally.

On the bwVisu nav-bar click `Interactive Apps` --> `RStusdio`. Than specify the resources and click `Launch`. This will open RStudio in your current web browser.

# Navigating RStudio
---

**The RStudio interface is divided into four main panes:**

- **Source Editor:** Where you write scripts and create documents.
- **Console:** Where you can run R commands interactively.
- **Environment/History:** Displays active variables and command history.
- **Files/Plots/Packages/Help:** Manages files, shows plots, manages packages, and provides R help.

**Basic Navigation:**

- **Files Tab:** Browse, open, and manage files in your RStudio project.
- **Plots Tab:** Visualize and manage graphical outputs from R.
- **Help Tab:** Access R documentation and help for packages.

# Working with R Packages
---

To install a new package in RStudio, you can use the install.packages() function in the Console pane. For example, to install the ggplot2 package:

```R
install.packages("ggplot2")
```

After installing a package, load it into the session to use its functions:

```R
library(ggplot2)
```

# Writing and Running Code
---

Click on `File` --> `New File` --> `R Script` --> to open a new script tab in the Source Editor. Or click ++ctrl+alt+shift+"N"++ to open a script. You can run R code directly in the Console, or write your code in the Source Editor and run it by pressing ++ctrl+enter++. To run the entire script, use the Source button. Example R code to plot data:

```{.R linenums="1" title="R"}
data <- data.frame(x = 1:10, y = rnorm(10))
plot(data$x, data$y, main = "Random Scatterplot", xlab = "X Axis", ylab = "Y Axis")
```

# Advanced Features
---

**R Markdown** allows you to combine narrative, code, and output into a single document. Create a new R Markdown file via `File` --> `New File` --> `R Markdown`. This document can be rendered into HTML, PDF, or Word.

## Using Shiny
---

Shiny is a package that allows you to build interactive web apps straight from R. Start a new Shiny app via `File` --> `New File` --> `Shiny Web App`.

Example basic Shiny application:

```{.R linenums="1" title="R"}
library(shiny)
ui <- fluidPage(
  sliderInput("slider", "Choose a number", 1, 100, 50),
  textOutput("result")
)
server <- function(input, output) {
  output$result <- renderText({ paste("You selected", input$slider) })
}
shinyApp(ui = ui, server = server)
```

Shiny is particularly well-suited for turning statistical analyses into interactive visualization apps, which can be an excellent way for data scientists to communicate their findings non-technically.

# Package Development
---

Studio supports the development of R packages, providing tools to:

- **Build, Test, and Document Packages:** Simplify the process of package creation with integrated tools for testing and documenting your code.
- **Roxygen2 Integration:** Use Roxygen2 comments for easier documentation of functions and data.
