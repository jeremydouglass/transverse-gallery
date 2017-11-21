build:
	bundle exec jekyll build --config _config-travis.yml

buildproof: build proof

proof: 
	htmlproofer ./_site --disable-external

serve:
	bundle exec jekyll serve --config _config-travis.yml  --incremental

view:
	open http://127.0.0.1:4000
