<script setup lang="ts">
 import { ref, computed, watch } from 'vue'
 import { searchTypes } from "@/model/searchTypes.ts";

 const emit = defineEmits(['searchType', 'searchString', 'searchRequested'])

const searchType = ref(searchTypes.CNPJ)
const searchString = ref("");

const inputMode = computed(()=>{
  if(searchType.value === searchTypes.CNPJ){
    return 'numeric'
  }
  return 'text'
})

const inputPatten = computed(()=>{
  if(searchType.value === searchTypes.CNPJ || searchType.value === searchTypes.REGISTRO_ANS){
    return '[0-9]*'
  }
  return ''
})

const searchHint = computed(() => {
  switch (searchType.value) {
    case searchTypes.CNPJ:
      return 'CNPJ: 12345678000199'
    case searchTypes.RAZAO_SOCIAL:
      return 'RAZÃO SOCIAL: REDE MEDICA LTDA'
    case searchTypes.NOME_FANTASIA:
      return 'NOME FANTASIA: REDE MEDICA NORDESTE'
    case searchTypes.REGISTRO_ANS:
      return 'REGISTRO NA ANS: 4123456'
  }
})

const extraHintClass = computed(() => {
  if (searchString.value !== '') {
    return "extraHintClass"
  }
  return "disabled"
})

const inputSanitization = (e : Event) => {
  const input = e.target as HTMLInputElement;
  if (searchType.value === searchTypes.CNPJ || searchType.value === searchTypes.REGISTRO_ANS){
    input.value = input.value.replace(/\D/g, '');
    searchString.value = input.value;
  } else {
    searchString.value = input.value;
  }
}

const clearCNPJIfNeeded = () => {
  if (searchType.value === searchTypes.CNPJ || searchType.value === searchTypes.REGISTRO_ANS){
    searchString.value = searchString.value.replace(/\D/g, '');
  }
}

watch(searchType,() => {
  emit('searchType', searchType.value);
});

watch(searchString, () => {
  emit('searchString', searchString.value);
})

</script>

<template>
  <div class="container">
    <div :class="extraHintClass">
      {{searchHint}}
    </div>
    <div class="bottom">
    <input class="search-input"
               type="text"
               :pattern="inputPatten"
               :inputmode="inputMode"
               :placeholder="searchHint"
               v-model="searchString"
               @input="inputSanitization"
               @keyup.enter="$emit('searchRequested')"
        />
    <select class="select-search" @change="clearCNPJIfNeeded" v-model="searchType">
      <option :value="searchTypes.CNPJ" selected >CNPJ</option>
      <option :value="searchTypes.REGISTRO_ANS">Registro na ANS</option>/
      <option :value="searchTypes.RAZAO_SOCIAL">Razão Social</option>
      <option :value="searchTypes.NOME_FANTASIA">Nome Fantasia</option>
    </select>
    </div>
  </div>
</template>

<style scoped>
.disabled{
  opacity: 0;
}

.container{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: end;
}

.bottom{
  display: flex;
  gap: 1rem;
  height: 50%;

}

.search-input{
  width: calc(100% - 10rem);
  font-size: 12pt;
  padding-left: 0.5rem;
}

.select-search{
  width: 8rem;
}

.extraHintClass{
  color: gray;
  margin-bottom: 0.5rem;
}
</style>