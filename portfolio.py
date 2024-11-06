import streamlit as st

# Função para carregar a foto do desenvolvedor
def load_image(image_path):
    return st.image(image_path, use_column_width=True)

# Função para exibir o currículo
def exibir_curriculo():
    st.header("Currículo Profissional")
    
    # Resumo das qualificações
    st.subheader("Resumo das Qualificações")
    st.write("""
    Profissional com experiência sólida em desenvolvimento de software, 
    com foco em criação de soluções eficientes e escaláveis. Expertise em 
    tecnologias web, front-end, back-end e desenvolvimento de aplicativos 
    móveis. Capacidade comprovada de trabalhar em equipe e gerenciar projetos 
    de software de ponta a ponta, do planejamento à entrega.
    """)
    
    # Experiência Profissional
    st.subheader("Experiência Profissional")
    st.write("""
    **-[Desenvolvimento e manutenção de sistemas utilizando Python, focando em automação de processos, análise de dados e integração com APIs.]
[-Criação de scripts e programas para automação de tarefas repetitivas e melhoria de fluxos de trabalho, resultando em uma redução de 40% no tempo de execução de processos internos.]
[-Utilização de frameworks como Django e Flask para construção de aplicações web escaláveis e seguras.]
[-Desenvolvimento de ETL (Extração, Transformação e Carga) para integrar dados de diferentes fontes em um data warehouse.]
[-Aplicação de técnicas de análise de dados com bibliotecas como Pandas, NumPy e Matplotlib para gerar relatórios e dashboards customizados.]
[-Trabalho com integração de sistemas através de APIs RESTful e SOAP.]
[-Implementação de testes automatizados com PyTest, garantindo a qualidade e robustez do código.]
[-Colaboração com equipes multidisciplinares, incluindo designers, analistas de dados e gestores de projetos, para entregar soluções eficientes dentro dos prazos estabelecidos.]
[-Monitoramento e otimização de desempenho de sistemas, utilizando ferramentas como Celery para tarefas assíncronas e Redis para caching.]
Principais Tecnologias e Ferramentas:

-Linguagens: Python, SQL
-Frameworks: Django, Flask
-Bibliotecas: Pandas, NumPy, Matplotlib, Requests, PyTest
-Banco de Dados: MySQL, PostgreSQL, SQLite
-Ferramentas de DevOps: Docker, Jenkins, Git
-Outras: Celery, Redis, API RESTful
.
    """)
    
    # Educação
    st.subheader("Educação")
    st.write("""
    **cursando em Engenharia de softare**  
    Universidade unicesumar em Araraquara (SP)
    """)

    # Habilidades Técnicas
    st.subheader("Habilidades Técnicas")
    st.write("""
    - **Linguagens de Programação:** Python,
    -
    """)

    # Projetos e Realizações
    st.subheader("Projetos e Realizações")
    st.write("""
    - **Sistema de Gestão de Tarefas (React, Node.js)**: Aplicação web que permite o gerenciamento de tarefas, com autenticação de usuário e persistência de dados em um banco de dados MongoDB.
    - **Aplicativo de Clima (Flutter)**: Aplicativo móvel que exibe a previsão do tempo utilizando APIs públicas e design responsivo.
    - **E-commerce de Produtos Digitais (Vue.js, Firebase)**: Plataforma de vendas online com integração de pagamento, carrinho de compras e recomendação de produtos.
    """)

    # Idiomas
    st.subheader("Idiomas")
    st.write("""
    - **Português** (Nativo)
    - **Inglês** (medio)
    """)

    # Cursos e Treinamento
    st.subheader("Cursos e Treinamentos")
    st.write("""
    - **Certificação em Python (senai)**
    - 
    """)

    # Referências Profissionais
    st.subheader("Referências Profissionais")
    st.write("""
    - **
    """)

    # Contato
    st.subheader("Contato")
    st.write("""
    - **Email:** lucasnacsimnento87@gmail.com
    - **LinkedIn:** [linkedin.com/in/desenvolvedor](https://www.linkedin.com/in/)
    - **GitHub:** [github.com/desenvolvedor](https://github.com/)
    - **Site Pessoal:** [www.desenvolvedor.com](http://www.
    - **Telefone:**[16981619644]
               """)

# Função para exibir o portfólio de projetos
def exibir_portfolio():
    st.header("Portfólio de Projetos")
    
    # Lista de projetos com descrições
    projetos = [
        {"nome": "Sistema de Gestão de Tarefas", "tecnologias": "React, Node.js", "descricao": "Aplicação web para gerenciar tarefas, com autenticação e persistência em MongoDB."},
        {"nome": "Aplicativo de Clima", "tecnologias": "Flutter", "descricao": "Aplicativo móvel que fornece a previsão do tempo utilizando APIs públicas."},
        {"nome": "E-commerce de Produtos Digitais", "tecnologias": "Vue.js, Firebase", "descricao": "Plataforma de e-commerce com carrinho de compras e integração de pagamento."}
    ]
    
    for projeto in projetos:
        st.subheader(projeto["nome"])
        st.write(f"**Tecnologias:** {projeto['tecnologias']}")
        st.write(projeto["descricao"])

# Função principal para exibir o portfólio completo
def main():
    st.title("Portfólio de Desenvolvimento Online")
    
    # Menu lateral para navegação
    menu = st.sidebar.selectbox(
        "Navegue pelo conteúdo:",
        ("Início", "Currículo", "Portfólio")
    )
    
    # Carregar foto do desenvolvedor
    load_image("foto_do_desenvolvedor.jpg")  # Insira o caminho da sua foto aqui.
    
    # Exibição conforme a seleção no menu
    if menu == "Início":
        st.write("Bem-vindo ao meu portfólio! Navegue pelos menus à esquerda para conhecer mais sobre mim e meus projetos.")
    
    elif menu == "Currículo":
        exibir_curriculo()
    
    elif menu == "Portfólio":
        exibir_portfolio()

if __name__ == "__main__":
    main()
