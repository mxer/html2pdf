#! /bin/sh

CMD=../html2pdf.py
URL=https://github.com
FILE=sample.html

echo "Test 1: show help message"
${CMD} -h

echo "Test 2: execute CMD with no options"
${CMD}

echo "Test 3: Convert sample.html to sample.pdf with -f option"
OUT=sample.pdf
${CMD} -f ${FILE}
[ -f ${OUT} ] || (echo "error at Test 3"; exit)
\rm -f ${OUT}

echo "Test 4: Convert sample.html to sample-o.pdf with -f and -o option"
OUT=sample-o.pdf
${CMD} -f ${FILE} -o ${OUT}
[ -f ${OUT} ] || (echo "error at Test 4"; exit)
\rm -f ${OUT}

echo "Test 5: Convert https://github.com to github.pdf with -f option"
OUT=https-__github.com.pdf
${CMD} -u ${URL}
[ -f ${OUT} ] || (echo "error at Test 5"; exit)
\rm -f ${OUT}

echo "Test 6: Convert https://github.com to github-o.pdf with -f and -o option"
OUT=github-o.pdf
${CMD} -u ${URL} -o ${OUT}
[ -f ${OUT} ] || (echo "error at Test 6"; exit)
\rm -f ${OUT}

echo "Test 7: set -f and -u options"
${CMD} -f ${FILE} -u ${URL}

