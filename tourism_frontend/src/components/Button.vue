Vue.component('inputForm', {
  props: ['value', 'name'],
  data() {
    return {
      keyInputForm: null,
      thisValue: this.value
    }
  },
  template: `
    <div>
    <button v-if="!thisValue && !keyInputForm" @click="keyInputForm=true;thisValue=''">Добавить {{ name }}</button>
    <div>
      <h4 v-if="!keyInputForm" class="card-title" @click="keyInputForm = true">{{ value }}</h4>
      <input v-else type="text" :value="value" :name="name" v-model="thisValue" @input="$emit('input', thisValue)" @blur="keyInputForm = false;$emit('edit-field', $event)">
      </div>
    </div>
  `
})

new Vue({
  el: "#app",
  data: {
    dataObject: {
      name: 'Name',
      // surname: undefined,
      age: '17',
      id: 1
    }
  },
  methods: {
    editField(e) {
      console.clear();
      const value = e.target.value;
      const key = e.currentTarget.getAttribute('name');
      // axios.post(this.postURL, { user_id: this.dataObject.id, field_name: key, field_value: value })
      console.log('axios post => ', {
        user_id: this.dataObject.id,
        field_name: key,
        field_value: value
      })
    }
  }
})