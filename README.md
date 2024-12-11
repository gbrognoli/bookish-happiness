# bookish-happiness
O projeto em Python utiliza o algoritmo kNN com o dataset Iris para classificação
Ele inclui carregamento de dados, treinamento, avaliação e previsão para novos dados. 
Você pode testar e ajustar o número de vizinhos ou o dataset conforme necessário.

Etapa 1: Carregar o Dataset
Nesta etapa, usamos o dataset Iris, que é um conjunto de dados clássico para classificação. 
Ele contém 150 amostras de flores com 4 características cada (como comprimento e largura de sépala e pétala) e 3 classes de rótulos.

Etapa 2: Dividir o Dataset
Dividimos os dados em conjuntos de treinamento (70%) e teste (30%).
O random_state garante que a divisão seja reproduzível.
Isso é importante para treinar o modelo com uma parte dos dados e avaliar seu desempenho com outra parte.

Etapa 3: Escolher o Número de Vizinhos (k)
k define o número de vizinhos mais próximos que o modelo considerará ao fazer uma previsão.
Um valor típico para começar é 3, mas ele pode ser ajustado com base no desempenho.

Etapa 4: Inicializar e Treinar o Modelo kNN
Criamos um modelo kNN com KNeighborsClassifier da biblioteca scikit-learn.
Treinamos o modelo com os dados de treinamento (X_train e y_train).

Etapa 5: Fazer Previsões
Após o treinamento, usamos o modelo para prever as classes do conjunto de teste (X_test).
As previsões são armazenadas em y_pred.

Etapa 6: Avaliar o Modelo
Calculamos a acurácia comparando as previsões (y_pred) com os rótulos reais (y_test).
Geramos um relatório de classificação para avaliar métricas como precisão, recall e F1-score para cada classe.

Etapa 7: Fazer Previsões para Novos Dados
Preparamos um conjunto de dados não visto (amostras fictícias) para prever suas classes.
Usamos o modelo treinado para classificar essas amostras e traduzimos os resultados para os nomes das espécies.

Acurácia Perfeita
Acurácia é a proporção de predições corretas em relação ao total de predições. Neste caso, o modelo acertou todas as 45 amostras do conjunto de teste.
Por que isso aconteceu?
O dataset Iris é relativamente simples, com apenas 4 características bem definidas para separar as classes (Setosa, Versicolor e Virginica).
A classe Setosa, por exemplo, é claramente distinta das outras duas em termos de comprimento e largura das pétalas, o que facilita a separação.

Relatório de Classificação
Métricas apresentadas:
Precision: Proporção de amostras corretamente identificadas como pertencentes a uma classe específica. Todas estão em 1.0.
Recall: Proporção de amostras de uma classe que foram corretamente identificadas. Todas também estão em 1.0.
F1-Score: Média harmônica entre precisão e recall, usada como métrica equilibrada.
Support: Número de amostras reais de cada classe no conjunto de teste:
19 para Setosa.
13 para Versicolor.
13 para Virginica.
O que isso significa?

O modelo não teve nenhum erro para nenhuma das classes, indicando que a separação entre as classes no espaço de características é muito clara.

Previsões para Novas Amostras
O modelo previu corretamente as espécies:
A primeira amostra, com características pequenas, foi identificada como Setosa.
A segunda amostra, com características maiores e próximas de Virginica, foi identificada como Virginica.
Isso mostra que o modelo é robusto para prever corretamente amostras desconhecidas.

Limitações do Dataset
Apesar do excelente desempenho, o dataset Iris é relativamente pequeno e bem estruturado. Em problemas mais complexos:
Dados ruidosos ou características mal definidas podem reduzir a acurácia.
O modelo pode sofrer para separar classes menos distintivas.

Escolha do k
Usamos k=3, um número ideal para evitar:
Overfitting (modelo se adapta ao ruído com k muito baixo).
Underfitting (modelo fica muito genérico com k muito alto).


Conclusão
O desempenho perfeito do modelo kNN no dataset Iris ocorre porque:

O dataset tem classes bem definidas e características claras.
A separação geométrica entre as classes é facilmente identificada pelo modelo.
Se você desejar experimentar com outro dataset mais complexo ou testar diferentes valores de k, posso ajudar a ajustar o modelo. Isso seria interessante para avaliar como o kNN funciona em cenários reais!
