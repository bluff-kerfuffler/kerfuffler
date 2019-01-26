package main

import (
	"log"
	"net/http"
)
import "github.com/google/uuid"

func main() {
	init()
	http.HandleFunc("/verifadd/", verifAddHandler)
	http.HandleFunc("/verifadd/", verifAddHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func verifiedHandler(writer http.ResponseWriter, request *http.Request) {
	token := ""
	response := false
	updateVerifAdd(token, response)

}

func verifAddHandler(w http.ResponseWriter, r *http.Request) {
	token := generateToken()
	user := ""
	channel := ""
	storeVerifAdd(token, user, channel)
	_, err := w.Write([]byte(token))
	if err != nil {
		panic(err)
	}
}

func generateToken() string {
	return uuid.New().String()
}

