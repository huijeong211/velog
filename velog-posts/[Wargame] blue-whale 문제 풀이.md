<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.18</li>
<li>문제명: blue-whale</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/853">https://dreamhack.io/wargame/challenges/853</a></li>
<li>핵심 키워드: Docker, Docker Layer</li>
</ul>
<hr />
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제공된 도커 이미지를 다운로드하고 docker history 명령어를 확인하여 이미지 빌드 과정과 내부 동작을 분석하였다.</p>
<p><strong>Docker 이미지 가져오기</strong></p>
<pre><code>$ docker pull dreamhackofficial/blue-whale:1
1: Pulling from dreamhackofficial/blue-whale
Digest: sha256:6bcfd56d243ab37ede113aa8a6243eb3f274ae8971ff1eefc67796329c252fee
Status: Image is up to date for dreamhackofficial/blue-whale:1
docker.io/dreamhackofficial/blue-whale:1
</code></pre><p><strong>Dockerfile 및 빌드 히스토리 분석:</strong></p>
<p>docker history 명령어를 통해 이미지를 생성할 때 실행된 레이어별 명령어를 확인했다.</p>
<pre><code>$ docker history dreamhackofficial/blue-whale:1
IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
6bcfd56d243a   3 years ago   EXPOSE map[31337/tcp:{}]                        0B        buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   USER chall                                      0B        buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   WORKDIR /home                                   4.1kB     buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   RUN /bin/sh -c rm * # buildkit                  12.3kB    buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   RUN /bin/sh -c touch `python3 -c &quot;print(open…   12.3kB    buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   WORKDIR /home/chall                             4.1kB     buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   RUN /bin/sh -c chown -R root:$user /home/$us…   28.7kB    buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   COPY ./deploy/flag /home/chall/flag # buildk…   16.4kB    buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   RUN /bin/sh -c adduser $user # buildkit         406kB     buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   RUN /bin/sh -c apt-get install -y python3 # …   33.4MB    buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   RUN /bin/sh -c apt-get update # buildkit        43.8MB    buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   ENV chall_port=31337                            0B        buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   ENV user=chall                                  0B        buildkit.dockerfile.v0
&lt;missing&gt;      3 years ago   /bin/sh -c #(nop)  CMD [&quot;bash&quot;]                 0B        
</code></pre><p>RUN touch ... 레이어</p>
<pre><code>&lt;missing&gt;      3 years ago   RUN /bin/sh -c touch `python3 -c &quot;print(open…   12.3kB    buildkit.dockerfile.v0</code></pre><p>python3 코드가 실행되며 /home/chall/flag 내용을 읽은 뒤, 그 플래그 문자열을 파일명으로 하는 빈 파일을 만들었다.</p>
<p>→결과: 해당 레이어의 layer.tar 내부에 /home/chall/FLAG{...} 형태의 파일이 물리적으로 기록됨.</p>
<p>RUN rm * 레이어 (바로 위 레이어)</p>
<pre><code>&lt;missing&gt;      3 years ago   RUN /bin/sh -c rm * # buildkit                  12.3kB    buildkit.dockerfile.v0</code></pre><p>/home/chall/ 디렉터리 내 파일들을 삭제했다.</p>
<p>→ 결과: 이 레이어에는 *&quot;해당 파일들을 화면에서 숨긴다&quot;*라는 표시(Whiteout)만 추가될 뿐, 아래 RUN touch 레이어 tarball에 저장된 파일은 전혀 영향받지 않는다.</p>
<hr />
<h2 id="3-문제-해결-과정-터미널-실습">3. 문제 해결 과정 (터미널 실습)</h2>
<p>히스토리를 확인해보니 도커는 삭제(rm)된 파일이라도 이전 레이어(Layer)에는 데이터가 그대로 남아있다. 레이어를 직접 뜯어보기 위해 이미지를 .tar 파일로 만든다.</p>
<ol>
<li>새 작업 디렉터리 생성 및 이동, 도커 이미지를 tar 파일로 추출 후 tar 파일 압축 해제한다.</li>
</ol>
<pre><code>user@user-VirtualBox:~/Downloads/fa75f8ae-5a42-43d2-af1f-76bf6d446ae9$ mkdir ~/whale_practice &amp;&amp; cd ~/whale_practice
mkdir: /home/user/whale_practice: File exists
user@user-VirtualBox:~/Downloads/fa75f8ae-5a42-43d2-af1f-76bf6d446ae9$ docker save dreamhackofficial/blue-whale:1 -o whale.tar
user@user-VirtualBox:~/Downloads/fa75f8ae-5a42-43d2-af1f-76bf6d446ae9$ tar -xvf whale.tar
blobs/
blobs/sha256/
blobs/sha256/27795aba362d5a047b7579f7e204c4e608fe6e7717e3bf9c9a0129944263e522
blobs/sha256/382b42bad09db4c48df3302e2871bd4e7a16567204a83e9dae58a67da0d3fd5f
blobs/sha256/6bcfd56d243ab37ede113aa8a6243eb3f274ae8971ff1eefc67796329c252fee
blobs/sha256/6e3729cf69e0ce2de9e779575a1fec8b7fb5efdfa822829290ab6d5d1bc3e797
blobs/sha256/72d2dc9f485f68e8e371d3ae37a168190b1c57ecd4d378ef4c65d285ff4e24e5
blobs/sha256/87a96c7a8db0a631faf4a5e0be8bd3d709919578eaea6f3a95816d2bc42d3715
blobs/sha256/957e6ff405005eb74839251944dc61304a8f2647d0f9f6b5b0e4c33bb4c9d3b3
blobs/sha256/a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4
blobs/sha256/cfff9de3e1e7f0c6139a00be6e8c8876156fbda40948c081c2b24f84025fadcb
blobs/sha256/e0c144699be7a3944553d1d9cd5ea78b7affb4c9f01705ca6251f5dfd7b44f5d
blobs/sha256/fb90d72728f232dc0c7595902d171e37e9d2a8e3e3bafd1ec5445ab0aa05ef36
index.json
manifest.json
oci-layout
</code></pre><p>이제 각 레이어의 압축을 풀기 위해 압축을 풀 디렉터리를 생성하고 이동해서 모든 레이어의 압축을 해제했다.</p>
<pre><code>user@user-VirtualBox:~/Downloads/fa75f8ae-5a42-43d2-af1f-76bf6d446ae9$ mkdir extracted &amp;&amp; cd extracted
user@user-VirtualBox:~/Downloads/fa75f8ae-5a42-43d2-af1f-76bf6d446ae9/extracted$ for f in ../blobs/sha256/*; do tar -xzf &quot;$f&quot; 2&gt;/dev/null; done
</code></pre><p>(오류 메시지 생략 위해 2&gt;/dev/null)</p>
<p>드디어 플래그 찾기.</p>
<pre><code>user@user-VirtualBox:~/Downloads/fa75f8ae-5a42-43d2-af1f-76bf6d446ae9/extracted$ find . -name &quot;DH{*&quot; 2&gt;/dev/null
./home/chall/DH{b06cb27a502a831822f927562258c6f69b5996a9916206cdb8755cc90ebf3b9f}
</code></pre><hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<p>소스코드의 주요 동작 원리는 다음과 같다.</p>
<ol>
<li><p><strong>명령어 치환을 이용한 파일 생성 (touch \python3 ...``):</strong> </p>
<ul>
<li>파이썬 스크립트 실행 결과인 플래그 문자열이 touch 명령어의 인자로 전달되면서 /home/chall/ 디렉터리 내에 DH{...} 형태의 파일명을 가진 빈 파일이 생성된다.</li>
</ul>
</li>
<li><p><strong>상위 레이어에서의 파일 삭제 (rm *):</strong></p>
<ul>
<li>다음 레이어에서 rm *이 실행되어 컨테이너 구동 시에는 파일이 삭제된 것으로 보인다.</li>
</ul>
</li>
<li><p><strong>도커 레이어 보존 특성 (docker save):</strong></p>
<ul>
<li>도커의 Union File System 특성상 상위 레이어의 rm 삭제 처리는 하위 레이어의 파일 데이터를 실제로 지우는 것이 아니라 은폐(Whiteout) 처리만 수행한다.</li>
<li>따라서 docker save로 전체 레이어의 아카이브를 추출해 이전 레이어를 해제하면 지워지기 전 상태의 DH{...} 파일명을 확인할 수 있다.</li>
</ul>
</li>
</ol>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>Docker Image Layer 구조 체득:</strong> 도커 이미지가 레이어 단위로 독립적인 압축 파일로 관리된다는 원리를 직접 아카이브 해제를 통해 확인했다.</li>
<li><strong>Union File System 보안 특성 이해::</strong> 도커 빌드 과정 중 상위 레이어에서 rm으로 민감한 파일(비밀키, 인증서, 플래그 등)을 삭제하더라도 이전 레이어 아카이브 분석을 통해 완전히 복원될 수 있음을 알게 되었다.</li>
</ul>