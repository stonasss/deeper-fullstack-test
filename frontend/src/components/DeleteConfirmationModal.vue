<template>
    <div v-if="isOpen" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(5px); z-index: 999;">
    </div>

    <div v-if="isOpen" @input="$emit('update:isOpen', $event)" style="position: fixed; top: 20%; left: 50%; transform: translateX(-50%); z-index: 1000; width: 400px;">
        <v-card>
            <v-card-title>Confirm Delete</v-card-title>
            <v-card-text>
                Are you sure you want to delete this user?
            </v-card-text>
            <v-card-actions>
                <v-btn @click="confirmDelete" color="error">Delete</v-btn>
                <v-btn @click="closeModal">Cancel</v-btn>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
export default {
    props: {
        isOpen: Boolean,
    },
    emits: ['update:isOpen', 'confirm', 'close'],
    methods: {
        confirmDelete() {
            this.$emit('confirm');
        },
        closeModal() {
            this.$emit('close');
        },
    },
};
</script>
