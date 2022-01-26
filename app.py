import pandas as pd 
import streamlit as st 
import numpy as np

st.title('Programação Aplicada!')
st.header('Este é um cabeçalho')
st.subheader('Este é um subcabeçalho')
st.text('Este é um texto simples')
st.markdown('Este Texto em **negrito** ou _itálico_')
st.markdown('[Este é um texto html](https://keilabcs.github.io/en/stable/api.html#display-text)',False)

#Esta é uma Tabela Interativa
df = pd.DataFrame(
	np.random.randn(5,10),
	columns=('coluna_%d' % i for i in range(10))
	)
st.dataframe(df)

# Esta é uma Tabela Estática
st.table(df)

# Este é um Botão 
if st.button('SUBMETER'):
   st.write(randint(0, 1000000))
else:
   st.write('Clique')

# Este é um radio
chute = st.radio(
    "Por que estudar programação?",
    ('Opção 1: Para ter ser um Médico!', 
    'Opção 2: Para ter ser um Enfermeiro! ', 
    'Opção 3: Para ter uma excelente carreira de TI!'))

if chute == 'Opção 3: Para ter uma excelente carreira de TI!':
    st.write('Correto!')
else:
    st.write("Errado, tente novamente.")

# Este é uma barra de arrastar
bar = st.slider('Isso é um slider',
				min_value=0,
				max_value=5,
				value=2,
				step=1)
st.write("Você Selecionou: ",bar)

# Isso é uma caixa de multiseleção
cx_mult = st.multiselect(
	'Selecione as colunas abaixos',
	df.columns
)
st.dataframe(df[cx_mult])

# Este é um Gráfico
df1 = pd.DataFrame(df, columns=['coluna_1','coluna_5','coluna_8'])
st.area_chart(df1)