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

const emit = defineEmits(['response', 'error'])

const responseData = ref(null);
const errorMessage = ref('');

const fetchData = async () => {
  const response = await fetchOperadoras(props.searchType, props.searchString, props?.desiredPage);
  if (typeof(response) === "string") {
    errorMessage.value = response;
  } else {
    responseData.value = response;
  }
}

const invalidCNPJSearchs = ["000", "0001"];
const isSearchEnable = computed(() => {
  if (props.searchType !== searchTypes.CNPJ && props.searchString.length > 2) {
    return true
  }

  if (props.searchType === searchTypes.CNPJ && !invalidCNPJSearchs.includes(props.searchString) && props.searchString.length > 2) {
    return true
  }

  return false
});

watch(responseData, () => {
  emit('response', responseData.value);
})

watch(errorMessage, () => {
  emit('error', errorMessage.value);
})
</script>

<template>
      <button @click="fetchData" :disabled="!isSearchEnable">
        Buscar
      </button>
</template>

<style scoped>

</style>