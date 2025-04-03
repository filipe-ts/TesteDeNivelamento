<script setup lang="ts">
 import { ref, computed, watch } from 'vue'
 import { searchTypes } from "@/model/searchTypes.ts";

 const emit = defineEmits(['searchType', 'searchString'])

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

watch(searchType,() => {
  emit('searchType', searchType.value);
});

watch(searchString, () => {
  emit('searchString', searchString.value);
})

</script>

<template>
  <div :class="extraHintClass">
    {{searchHint}}
  </div>
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
</template>

<style scoped>
.disabled{
  display: none;
}

.extraHintClass{
  color: gray;
}
</style>