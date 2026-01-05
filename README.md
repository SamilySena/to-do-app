# to-do-app
# 📝 To-Do App

Um aplicativo de gerenciamento de tarefas minimalista e moderno, desenvolvido em Python com interface gráfica Tkinter e banco de dados SQLite.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Sobre o Projeto

Este é um aplicativo completo para gerenciamento de tarefas (to-do list) com design clean e minimalista. Permite criar, editar, organizar e acompanhar suas tarefas diárias de forma simples e eficiente.

## ✨ Funcionalidades

- ✅ **Criar tarefas** com título, descrição e prioridade
- 🎨 **Organização por cores** - categorize suas tarefas visualmente
- 🔘 **Checkboxes redondos** para marcar tarefas concluídas
- ✏️ **Editar tarefas** existentes
- 🗑️ **Excluir tarefas** com confirmação
- 🎯 **Sistema de prioridades** (Alta, Média, Baixa)
- 🔍 **Filtros por cor** - visualize apenas tarefas de uma categoria
- 📊 **Estatísticas** - acompanhe total, pendentes e concluídas
- 💾 **Persistência de dados** - SQLite armazena tudo localmente
- 🕒 **Registro de datas** - criação e conclusão

## 🎨 Design

Interface minimalista com:
- Paleta de cores em tons pasteis
- Tipografia clean e legível
- Seletores circulares para conclusão
- Sistema de cores para categorização (vermelho, azul, verde, amarelo, roxo)
- Layout organizado e intuitivo

## 🚀 Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Tkinter** - Interface gráfica (GUI)
- **SQLite3** - Banco de dados
- **datetime** - Gerenciamento de datas

## 📋 Pré-requisitos

Apenas Python 3.8 ou superior instalado. Tkinter e SQLite já vêm inclusos no Python!

```bash
python --version  # Verificar versão do Python
```

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/todo-app.git
cd todo-app
```

2. Execute o aplicativo:
```bash
python main.py
```

Pronto! Nenhuma dependência externa necessária. 🎉

## 📁 Estrutura do Projeto

```
todo-app/
│
├── main.py              # Interface gráfica (GUI)
├── database.py          # Gerenciamento do banco de dados
├── tarefas.db          # Banco de dados SQLite (criado automaticamente)
├── README.md           # Documentação
└── LICENSE             # Licença MIT
```

## 💡 Como Usar

### Adicionar Tarefa
1. Preencha o título da tarefa
2. Adicione uma descrição (opcional)
3. Escolha a prioridade
4. Selecione uma cor para categorizar
5. Clique em "Adicionar"

### Editar Tarefa
1. Clique na tarefa desejada na tabela
2. Os campos serão preenchidos automaticamente
3. Faça as alterações
4. Clique em "Atualizar"

### Concluir Tarefa
1. Selecione a tarefa na tabela
2. Clique em "Concluir"
3. A tarefa será marcada com checkbox preenchido

### Filtrar por Cor
- Clique nos círculos coloridos na barra de filtros
- Visualize apenas tarefas da cor selecionada
- Clique no círculo cinza para ver todas

## 🗄️ Banco de Dados

O aplicativo utiliza SQLite com a seguinte estrutura:

**Tabela: tarefas**
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Identificador único (PRIMARY KEY) |
| titulo | TEXT | Título da tarefa |
| descricao | TEXT | Descrição detalhada |
| prioridade | TEXT | Alta, Média ou Baixa |
| cor | TEXT | red, blue, green, yellow, purple |
| status | TEXT | Pendente ou Concluída |
| data_criacao | TEXT | Data/hora de criação |
| data_conclusao | TEXT | Data/hora de conclusão |

## 🎓 Aprendizados

Este projeto foi desenvolvido para praticar:
- Desenvolvimento de interfaces gráficas com Tkinter
- Integração Python + SQLite
- Padrão de projeto MVC (Model-View-Controller)
- CRUD completo (Create, Read, Update, Delete)
- Gerenciamento de estado da aplicação
- Design minimalista e UX

## 🔮 Próximas Melhorias

- [ ] Sistema de busca por texto
- [ ] Ordenação por data/prioridade
- [ ] Exportação para CSV/JSON
- [ ] Temas claro/escuro
- [ ] Lembretes com notificações
- [ ] Categorias personalizáveis
- [ ] Subtarefas
- [ ] Integração com Google Calendar

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Samily Sena, Nycolle Khetlem e Katarine Meira

- GitHub: [@nomenome]
- LinkedIn: [Seu Nome]
  
- GitHub: [@nomenome]
- LinkedIn: [Seu Nome]
  
- GitHub: [@nomenome]
- LinkedIn: [Seu Nome]

## 🌟 Mostre seu apoio

Se este projeto te ajudou, dê uma ⭐️!

---

**Desenvolvido com ❤️ e Python**
