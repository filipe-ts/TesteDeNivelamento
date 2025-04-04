<script setup lang="ts">
import {computed, ref, watch} from "vue";
import { searchTypes } from "@/model/searchTypes.ts";
import axios from 'axios'
import type { SearchRequest } from "@/model/searchRequest";
import { fetchOperadoras } from "@/services/fetchOperadoras.ts"

const props = defineProps({
  searchType:{
    type: String,
    required: true,
  },
  searchString: {
    type: String,
    required: true,
  },
  desiredPage: {
    type: Number,
    required: false
  }
})


const emit = defineEmits(['response', 'error', 'searchEnable'])

const responseData = ref(null);
const errorMessage = ref('');

const fetchData = async () => {
  const response = await fetchOperadoras(props.searchType, props.searchString, props?.desiredPage);
  if (typeof(response) === "string") {
    errorMessage.value = response;
  } else {
    responseData.value = response;
    console.log(responseData.value);
  }
}

const invalidCNPJSearchs = ["000", "0001"];
const isSearchEnable = computed(() => {
  if (props.searchType !== searchTypes.CNPJ && props.searchString.length > 2) {
    emit('searchEnable', true);
    return true
  }

  if (props.searchType === searchTypes.CNPJ && !invalidCNPJSearchs.includes(props.searchString) && props.searchString.length > 2) {
    emit('searchEnable', true);
    return true
  }
  emit('searchEnable', false);
  return false
});

watch(responseData, () => {
  emit('response', responseData.value);
})

watch(errorMessage, () => {
  emit('error', errorMessage.value);
})

defineExpose({
  click: fetchData
});
</script>

<template>
      <button class="btn" @click="fetchData" :disabled="!isSearchEnable">
        Buscar
      </button>
</template>

<style scoped>
.btn{
  width: 8rem;
  background-color: #55ec93;
}

.btn:disabled{
  background-color: #b8b8b8;
}
</style>