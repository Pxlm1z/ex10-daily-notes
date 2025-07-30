<template>
  <div class="p-6 max-w-3xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">My Notes</h1>

    <div class="flex gap-2 mb-4">
      <input v-model="title" placeholder="Title" class="border p-2 w-1/3" />
      <input v-model="content" placeholder="Content" class="border p-2 flex-1" />
      <button @click="createNote" class="bg-green-500 text-white p-2">Add</button>
    </div>

    <NoteCard
      v-for="note in notes"
      :key="note.id"
      :note="note"
      @delete="deleteNote"
    />
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import NoteCard from '@/components/NoteCard.vue' // หากยังไม่ได้ import

const API_URL = import.meta.env.VITE_API_URL

const title = ref('')
const content = ref('')
const notes = ref([])

const fetchNotes = async () => {
  const token = localStorage.getItem('token')
  const res = await axios.get(`${API_URL}/api/notes`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
  notes.value = res.data
}

const createNote = async () => {
  const token = localStorage.getItem('token')
  try {
    await axios.post(`${API_URL}/api/notes`, {
      title: title.value,
      content: content.value
    }, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    title.value = ''
    content.value = ''
    fetchNotes()
  } catch (e) {
    console.error('Create note failed:', e)
  }
}

const deleteNote = async (id) => {
  const token = localStorage.getItem('token')
  await axios.delete(`${API_URL}/api/notes/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
  fetchNotes()
}

onMounted(fetchNotes)
</script>
