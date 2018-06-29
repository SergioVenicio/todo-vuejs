<template>
  <div class='ui card'>
    <div class="content" v-show="!isEditing">
      <div class='header'>
          {{ todo.title }}
      </div>
      <div class='meta'>
          {{ todo.project }}
      </div>
      <div class='extra content'>
          <span class='right floated edit icon' v-on:click="showForm">
          <i class='edit icon'></i>
        </span>
        <span class='right floated trash icon' v-on:click="deleteTodo(todo)">
          <i class='trash icon'></i>
        </span>
      </div>
    </div>
    <div class="content" v-show="isEditing">
      <div class='ui form'>
        <div class='field'>
          <label>Title</label>
          <input type='text' v-model="todo.title" >
        </div>
        <div class='field'>
          <label>Project</label>
          <input type='text' v-model="todo.project" >
        </div>
        <div class='ui two button attached buttons'>
          <button class='ui basic blue button' v-on:click="hideForm(todo)">
            Close X
          </button>
        </div>
      </div>
    </div>
    <div class='ui bottom attached green basic button' v-show="!isEditing &&todo.done" disabled>
        Completed
    </div>
    <div class='ui bottom attached red basic button' v-on:click="completeTodo(todo)" v-show="!isEditing && !todo.done">
        Pending
    </div>
  </div>
</template>

<script type="text/javascript">
import axios from 'axios'
import sweetalert from 'sweetalert'

export default {
  props: ['todo'],
  data () {
    return {
      isEditing: false
    }
  },
  methods: {
    completeTodo (todo) {
      axios.patch('http://localhost:8000/api/v1/todos/' + todo.id, {
        'done': true
      }).then(response => {
        sweetalert('Success!', 'To-Do created!', 'success')
        this.$emit('complete-todo', todo)
      }).catch(e => {
        console.log(e)
        sweetalert('Error!', 'To-Do complete error!', 'warning')
      })
    },
    deleteTodo (todo) {
      axios.delete('http://localhost:8000/api/v1/todos/' + todo.id, {}).then(response => {
        sweetalert('Success!', 'To-Do deleted!', 'success')
        this.$emit('delete-todo', todo)
      }).catch(e => {
        console.log(e)
        sweetalert('Error!', 'To-Do delete error!', 'warning')
      })
    },
    showForm () {
      this.isEditing = true
    },
    hideForm (todo) {
      axios.put('http://localhost:8000/api/v1/todos/' + todo.id, {
        'title': todo.title,
        'project': todo.project
      }).then(response => {
        sweetalert('Success!', 'To-Do edited!', 'success')
      }).catch(e => {
        console.log(e)
        sweetalert('Error!', 'To-Do edit error!', 'warning')
      })
      this.isEditing = false
    }
  }
}
</script>
