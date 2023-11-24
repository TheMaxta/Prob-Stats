enter_data <- function() {
    # Enter the data set here
    samp <- c(1.5 , 10.7 , 2.6 , 7.4 , 0.4 , 4.8 , 7.3 , 4.6 , 1.7 , 1.8 , 
              3.8 , 3.5 , 1.2 , 0.8 , 1.7 , 9.9 , 7.3 , 6.8 , 2.5 , 4.4 , 
              7.5 , 4.5 , 1.3 , 5.2, 10.6 , 0.7 , 3.5 , 1.3 , 1.5 , 5.3)
    return(samp)
}

library(distributions3)

#Statistical Analysis Functions: To compute mean, standard deviation, five-number summary, and perform a t-test.

compute_mean_sd <- function(data) {
    list(mean = mean(data), sd = sd(data))
}


#Plotting Functions: For boxplot, stem-and-leaf plot, and histogram.
compute_summary <- function(data) {
    fivenum(data)
}

perform_t_test <- function(data, mu = 5) {
    t.test(data, mu = mu)
}
create_boxplot <- function(data) {
    boxplot(data, horizontal = TRUE, xlab = "Minutes between foul shots")
}

create_stemplot <- function(data) {
    stem(data)
}

create_histogram <- function(data) {
    hist(data, freq = FALSE, xlab = "Minutes between foul shots", ylab = "Relative Frequency", breaks = 10*12:22)
}

#User Interface: This can be a simple textual interface in the console or a more complex GUI using a package like shiny.

main_menu <- function() {
    data <- enter_data()
    repeat {
        cat("\n1: Compute Mean and SD\n")
        cat("2: Compute Five-Number Summary\n")
        cat("3: Perform T-Test\n")
        cat("4: Create Boxplot\n")
        cat("5: Create Stem-and-Leaf Plot\n")
        cat("6: Create Histogram\n")
        cat("7: Exit\n")
        choice <- as.integer(readline(prompt = "Choose an option: "))

        if (choice == 1) {
            print(compute_mean_sd(data))
        } else if (choice == 2) {
            print(compute_summary(data))
        } else if (choice == 3) {
            print(perform_t_test(data))
        } else if (choice == 4) {
            create_boxplot(data)
        } else if (choice == 5) {
            create_stemplot(data)
        } else if (choice == 6) {
            create_histogram(data)
        } else if (choice == 7) {
            break
        } else {
            cat("Invalid option. Please try again.\n")
        }
    }
}
