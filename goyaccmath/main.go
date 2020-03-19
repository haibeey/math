package main
// This package is gotten from $GOPATH/src/golang.org/x/tools/cmd/goyacc/testdata/expr
import (
	"os"
)

func main() {
		var line []byte
		for _,w:= range os.Args[1:]{
			line = append(line,[]byte(w)...)
		} 
		yyParse(&exprLex{line: line})
}
