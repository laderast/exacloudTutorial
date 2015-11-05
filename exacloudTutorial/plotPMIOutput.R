fileName <- commandArgs()[1]

fileName <- "totalpmioutput.csv"
pmiTable <- read.csv(fileName)

pmiTable2 <- pmiTable[pmiTable$pmi_term1_w_word > 1 & pmiTable$pmi_term2_w_word > 1,]

pmiTable3 <- pmiTable2[sample(1:nrow(pmiTable2), 100),]

jpeg("pmiPlot.jpg")
plot(range(pmiTable3$pmi_term1_w_word), range(y=pmiTable3$pmi_term2_w_word))
wordcol <- ifelse(pmiTable3$pmi_term1_w_word > pmiTable3$pmi_term2_w_word, "blue", "orange" )
text(x = pmiTable3$pmi_term1_w_word, y=pmiTable3$pmi_term2_w_word, labels = pmiTable3$word, col=wordcol)
dev.off()
