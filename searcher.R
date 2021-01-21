library(tidyverse)
library(rvest)
library(Hmisc)

scraper <- function(website) {
  # this is the function that scrapes the websites, it just take as argument a single website and
  # returns the extracted text. The paste with collapse at the end is just because one of the websites
  # had lots of blank spaces between each paragraph and I wanted to get rid of them
  
  result <- read_html(website) %>%
    html_nodes("p") %>%
    html_text()
  
  return(paste(result, collapse=", "))
}


parse_info <- function(text, keywords) {
  # This is the actual regex parser, the final pattern is x|y|z[^./.]+ where x, y and z are 
  # the different keywords. It took me a while to understand the specifics of the list
  # returned by gregexpr, but it basically has an attribute match.length that can be extracted
  # with attr and that can be used to check if there was a match or not (there is some form of
  # report even in the case there is no match so I could not just check for the length > 0)
  
  subpattern <- paste(keywords, collapse="|")
  #print(subpattern)    this is here just for debugging because it took a while to find the right regex pattern
  reg_pattern <- paste0("(", subpattern, ")[^/.]+")
  #print(reg_pattern) # same as above
  filtered <- gregexpr(reg_pattern, 
                       text, 
                       perl=T, 
                       ignore.case=T)

  if (attr(filtered[[1]], "match.length") < 0){
    filtered <- list()
  }
  else {
    filtered <- regmatches(text, filtered)
    filtered <- paste(unlist(filtered), collapse="\n\n")
  }
  
  return(filtered)
}


search_info <- function(drugs, drug_bank_voc, keywords) {
  
  # The four websites have slightly different URLs which account for the different if statements
  # you see in this function: Wikipedia adds the capitalized name of whatever the page is for,
  # which is why I keep a capitalized version of the drug name in the capitalized_name variable;
  # drugs.com and rxlist just add the lower case name of the drug, but drugs.com has an .html at
  # the end; finally drugbank uses a so called DB code that I think is their own thing, but for which I
  # found a csv file (which is the drug_bank_voc in the arguments of the function).
  # The function then just takes the drug name, searches in those four websites for the keywords, parse
  # everything with parse_info and then saves the results in a directory called Drug_reports.
  # Now I wrote this code just for this exam, so I'm sorry if I hardcoded the directory name here, it
  # would also make sense to have the user specify the directory in the arguments of the function
  # but again I wrote this just for my computer so I didn't go that far :)
  
  webpages <- c("https://www.drugs.com/monograph/",
                "https://go.drugbank.com/drugs/",
                "https://www.rxlist.com/",
                "https://en.wikipedia.org/wiki/")
  
  for(drug in drugs) {
    drug <- gsub(" ", "", drug)
    report <- c()
    capitalized_name <- capitalize(drug)  # in the csv file for the DB codes they use capitalized names
    
    drug_bank_id <- drug_bank_db %>%
      filter(`Common name` == capitalized_name) %>%
      pull(`DrugBank ID`)
    
    for(webpage in webpages) {
      cat("\n")
      if(webpage == "https://go.drugbank.com/drugs/") {
        full_url <- paste0(webpage, drug_bank_id)
      }
      else if(webpage == "https://www.rxlist.com/") {
        full_url <- paste0(webpage, drug, "-drug.htm")
      }
      else if(webpage == "https://en.wikipedia.org/wiki/"){
        full_url <- paste0(webpage, capitalized_name)
      }
      else {
        full_url <- paste0(webpage, drug, ".html")
      }
      extracted_test <- try(scraper(full_url))     # the website may not exist, so the try() is here to catch the 404 errors
      print(full_url)
      relevant <- parse_info(extracted_test, keywords) # possible parsing of the error string
      if(length(relevant)>0){
        relevant <- paste0(toupper(full_url), "\n\n", relevant, "\n\n\n")
        report <- c(report, relevant)
      }
    }
    if(length(report)>0){
      write(report, file=paste0("./Drugs_reports/", drug, ".txt"))
    }
  }
}



setwd("~/Bioinfo_assignment/Final")

keywords <- c("thyroid", "iodine", "papillary", "follicular", "medullary", "anaplastic",
              "radiation", "euthyroid", "hyperthyroid", "hypothyroid", "calcitonin", "t3", "t4", 
              "triiodothyronine", "thyroxine", "goitre", "hurtle", 
              "cowden", "orphan annie", "hashimoto", "men2", "thyroglobulin")

drugs_db <- read_delim("./Saverunner/Results/network/txtFile/Drug_Disease_network_pval0.05.txt",
                  col_names=T,
                  delim="\t")

drugs <- drugs_db %>%
  arrange(desc(adjusted_similarity)) %>%
  pull(drug)


drug_bank_db <- read_csv("./drugbank_vocabulary.csv",
                         col_names = T)

search_info(drugs, 
            drug_bank_voc=drug_bank_db, 
            keywords=keywords)

