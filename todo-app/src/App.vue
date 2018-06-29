<template>
  <div id="app">
    <h1 class="ui dividing centered huge header">Todo list</h1>
    <div class="wrapper"></div>
    <div class='ui one column grid'>
      <div>
        <todo-list v-bind:todos="todos"></todo-list>
        <create-todo v-on:create-todo="createTodo"></create-todo>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import sweetalert from 'sweetalert'
import TodoList from './components/TodoList'
import CreateTodo from './components/CreateTodo'

export default {
  name: 'app',
  components: {
    TodoList,
    CreateTodo
  },
  data () {
    return {
      todos: []
    }
  },
  created () {
    axios.get('http://localhost:8000/api/v1/todos').then(response => {
      this.todos = response.data
    })
  },
  methods: {
    createTodo (newTodo) {
      axios.post('http://localhost:8000/api/v1/todos', {
        title: newTodo.title,
        project: newTodo.project,
        done: newTodo.done
      }).then(response => {
        this.todos.push(newTodo)
        sweetalert('Success!', 'To-Do created!', 'success')
      }).catch(e => {
        console.log(e)
        sweetalert('Error!', 'To-Do created error!', 'danger')
      })
    }
  }
}
</script>

<style>
.grid {
  padding-left: 1rem!important;
}
.header {
  margin-top: 0.5rem!important;
  margin-bottom: 0.5rem!important
}
.wrapper {
  padding: 1rem;
}
</style>
