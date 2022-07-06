SyntaxError: /tmp/python-converter/pegt7h2ll3ah6wxt/Hello.js: Unexpected token (3:8)

  1 | import * as time from 'time';
  2 | import * as pygame from 'pygame';
> 3 | import {*} from 'pygame/locals';
    |         ^
  4 | import * as random from 'random';
  5 | var _pj;
  6 | var game;
    at Parser._raise (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:476:17)
    at Parser.raiseWithData (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:469:17)
    at Parser.raise (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:430:17)
    at Parser.unexpected (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:3789:16)
    at Parser.parseIdentifierName (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:13564:18)
    at Parser.parseIdentifier (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:13544:23)
    at Parser.parseModuleExportName (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:15693:17)
    at Parser.parseNamedImportSpecifiers (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:15883:33)
    at Parser.parseImport (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:15703:39)
    at Parser.parseStatementContent (/usr/local/nvm/versions/node/v14.0.0/lib/node_modules/@babel/core/node_modules/@babel/parser/lib/index.js:14223:27) {
  loc: Position { line: 3, column: 8, index: 72 },
  pos: 72,
  code: 'BABEL_PARSE_ERROR',
  reasonCode: 'UnexpectedToken'
}
