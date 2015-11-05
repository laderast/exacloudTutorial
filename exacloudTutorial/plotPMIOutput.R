cmdArgs <- commandArgs(TRUE)
fileName <- cmdArgs[1]
word1 <- cmdArgs[2]
word2 <- cmdArgs[3]

fileName <- "totalpmioutput.csv"
pmiTable <- read.csv(fileName)

pmiTable2 <- pmiTable[pmiTable$pmi_term1_w_word > 1 & pmiTable$pmi_term2_w_word > 1,]

pmiTable3 <- pmiTable2[sample(1:nrow(pmiTable2), 100),]

pdf("pmiPlot.pdf", width=8, height=8)
plot(range(pmiTable3$pmi_term1_w_word), range(y=pmiTable3$pmi_term2_w_word), 
     xlab=paste0(word1,"-PMI"), ylab=paste0(word2, "-PMI"))
wordcol <- ifelse(pmiTable3$pmi_term1_w_word > pmiTable3$pmi_term2_w_word, "blue", "orange" )
text(x = pmiTable3$pmi_term1_w_word, y=pmiTable3$pmi_term2_w_word, labels = pmiTable3$word, col=wordcol)
dev.off()
