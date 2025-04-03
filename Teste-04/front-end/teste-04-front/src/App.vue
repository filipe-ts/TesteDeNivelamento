<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, computed } from 'vue'

enum searchTypes {
  CNPJ = 'CNPJ',
  RAZAO_SOCIAL = 'Razao_Social',
  NOME_FANTASIA = 'Nome_Fantasia'
}

const searchType = ref(searchTypes.CNPJ)
const searchString = ref("");

const inputMode = computed(()=>{
  if(searchType.value === searchTypes.CNPJ){
    return 'numeric'
  }
  return 'text'
})

const inputPatten = computed(()=>{
  if(searchType.value === searchTypes.CNPJ){
    return '[0-9]*'
  }
  return ''
})

const searchHint = computed(() => {
  switch (searchType.value) {
    case searchTypes.CNPJ:
      return 'EX: 12345678000199'
    case searchTypes.RAZAO_SOCIAL:
      return 'EX: REDE MEDICA LTDA'
    case searchTypes.NOME_FANTASIA:
      return 'EX: REDE MEDICA NORDESTE'
  }
})

const extraHintClass = computed(() => {
  if (searchString.value !== '') {
    return "extraHintClass"
  }
  return "disabled"
})

const invalidCNPJSearchs = ["000", "0001"]
const isSearchEnable = computed(() => {

  if (searchType.value !== 'CNPJ' && searchString.value.length > 2) {
    return true
  }

  if (searchType.value === 'CNPJ' && !invalidCNPJSearchs.includes(searchString.value) && searchString.value.length > 2) {
    return true
  }

  return false
});

const printStates = () => {
  console.log(searchType.value)
  console.log(searchString.value)
  console.log(isSearchEnable.value)
  console.log(inputMode.value)
  console.log(inputPatten.value)
}

const inputSanitization = (e : Event) => {
  const input = e.target as HTMLInputElement;
  if (searchType.value === searchTypes.CNPJ){
    input.value = input.value.replace(/\D/g, '');
    searchString.value = input.value;
  } else {
    searchString.value = input.value;
  }
}

const clearCNPJIfNeeded = () => {
  if (searchType.value === searchTypes.CNPJ){
    searchString.value = searchString.value.replace(/\D/g, '');
  }
}
</script>

<template>
  <header>
    Busca ANS
  </header>
  <search>
    <div :class="extraHintClass">
      {{searchHint}}
    </div>
    <div>
      <input class="search-input"
             type="text"
             :pattern="inputPatten"
             :inputmode="inputMode"
             :placeholder="searchHint"
             v-model="searchString"
             @input="inputSanitization"
      />
      <select class="select-search" @change="clearCNPJIfNeeded" v-model="searchType">
        <option :value="searchTypes.CNPJ" selected >CNPJ</option>
        <option :value="searchTypes.RAZAO_SOCIAL">Razão Social</option>
        <option :value="searchTypes.NOME_FANTASIA">Nome Fantasia</option>
      </select>
      <button @click="printStates" :disabled="!isSearchEnable">
        Buscar
      </button>
    </div>

  </search>

<!--      <nav>-->
<!--        <RouterLink to="/">Home</RouterLink>-->
<!--        <RouterLink to="/about">About</RouterLink>-->
<!--      </nav>-->
<!--  <RouterView />-->
</template>

<style scoped>
.disabled{
  display: none;
}

.extraHintClass{
  color: lightgray;
}
</style>
