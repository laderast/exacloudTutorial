##let's call this file runRJob.R
library(R.utils)
i <- as.numeric(cmdArg("i"))

#need to add 1 to i value because HTCondor starts with 0 for indexing and
#R starts with 1
i <- i + 1
inputDir <- cmdArg("inputDir")

print(inputDir)

#inputDir <- paste0(getwd(),"/",inputDir)
#List files in inputDirectory
#we use "$" here in case there are output files
fileList <- list.files(inputDir, pattern = ".csv$",full.names=TRUE)
fileToRun <- fileList[i]

print(fileList)

#... do some stuff with the fileToRun
tab <- read.csv(fileToRun)

#remove first column
tab <- tab[,-1]
output <- apply(tab, 2, mean)

#save the output as TSV based on file name
fileOut <- paste0(fileToRun, ".out.tsv")
write.table(output, file=fileOut, sep="\t", quote=F, row.names=F)
