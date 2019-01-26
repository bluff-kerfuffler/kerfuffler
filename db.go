package main

type verify struct {
	token string
	user string
	channel string
	verified int
}

var verifMap map[string]verify

func updateVerifAdd(token string, response bool) {

}

func storeVerifAdd(token string, user string, channel string) {

}

func init() {
	verifMap = make(map[string]verify)
}
