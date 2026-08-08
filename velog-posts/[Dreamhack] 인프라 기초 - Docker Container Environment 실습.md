<p><strong>학습일:</strong> 2026년 07월 01일
<strong>문제 링크:</strong> <a href="https://dreamhack.io/wargame/challenges/876">https://dreamhack.io/wargame/challenges/876</a></p>
<hr />
<h2 id="📌-1-핵심-개념-요약">📌 1. 핵심 개념 요약</h2>
<ul>
<li><strong>주요 개념:</strong> Dockerfile 이미지 빌드(<code>build</code>), 컨테이너 구동(<code>run</code>), 내부 컨테이너 진입(<code>exec</code>)</li>
<li><strong>한 줄 요약:</strong> 제공된 Dockerfile 구조를 분석한 뒤, 로컬 호스트 환경에서 도커 클라이언트를 이용해 직접 가상 컨테이너 환경을 구축하고 내부 파일 시스템에 격리된 플래그 데이터를 안전하게 추출함.</li>
</ul>
<hr />
<h2 id="🔍-2-문제">🔍 2. 문제</h2>
<ul>
<li><strong>개요:</strong> &quot;주어진 Dockerfile을 빌드하여 이미지를 생성하고 컨테이너를 실행해 보세요!&quot;라는 인프라 실습 과제가 주어짐.</li>
<li><strong>목표:</strong> 도커 기본 명령어 스택(Build, Run, Exec)을 정확히 이해하고 사용법을 숙지하여, 가상 머신 시스템 내부 권한을 확보하고 <code>DH{...}</code> 플래그를 획득해야 함.</li>
</ul>
<hr />
<h2 id="🚀-3-해결-과정">🚀 3. 해결 과정</h2>
<h3 id="1단계-dockerfile-지시자-해석">1단계: Dockerfile 지시자 해석</h3>
<ul>
<li>제공된 Dockerfile 분석 결과, <code>FROM ubuntu:22.04</code> 환경 위에 일반 유저 <code>chall</code> 계정을 생성하고, 대기 포트 <code>2222</code>번을 사용해 <code>socat</code>으로 특정 서비스를 바인딩하는 구조임을 확인함.</li>
<li>호스트 환경에 동봉된 <code>flag</code> 데이터가 컨테이너 빌드 시 내부 디렉토리인 <code>/home/chall/flag</code> 경로로 안전하게 이관된다는 파일 인프라 흐름을 도출함.</li>
</ul>
<h3 id="2단계-로컬-도커-가상-인프라-핸들링">2단계: 로컬 도커 가상 인프라 핸들링</h3>
<ul>
<li>윈도우 파워셸 환경에서 <code>Dockerfile</code>이 위치한 빌드 콘텍스트로 이동한 뒤 아래 명령어를 수행함:<ol>
<li><strong>도커 이미지 빌드:</strong> <code>docker build -t dh-practice .</code> (현재 폴더의 레시피를 기반으로 무결한 이미지 레이어 빌드)</li>
<li><strong>컨테이너 데몬 구동:</strong> <code>docker run -d -p 2222:2222 --name my-container dh-practice</code> (백그라운드 격리 환경에서 가상 프로세스 정상 구동 확인)</li>
</ol>
</li>
</ul>
<h3 id="3단계-컨테이너-내부-침투-및-플래그-획득">3단계: 컨테이너 내부 침투 및 플래그 획득</h3>
<ul>
<li>실행 중인 컨테이너 인프라 내부로 직접 명령어를 주입하기 위해 <code>docker exec -it my-container /bin/bash</code> 치트키 명령어를 실행함.</li>
<li>외부 호스트 파워셸에서 도커 내부 우분투 리눅스 셸(Shell) 권한으로 전환 성공함.</li>
<li><code>Dockerfile</code>에서 명시했던 타겟 경로인 <code>/home/chall/</code> 디렉토리로 이동 후 <code>cat flag</code> 명령어를 입력하여 격리벽 내부에 안전하게 하드코딩되어 보관 중이던 진짜 <strong><code>DH{...}</code></strong> 플래그를 획득함.</li>
</ul>
<hr />
<h2 id="📝-4-오늘의-삽질--복기">📝 4. 오늘의 삽질 &amp; 복기</h2>
<ul>
<li><strong>어려웠던 점 / 막혔던 부분:</strong> 처음에는 드림핵 문제 페이지에 호스트 주소와 외부 개방 포트가 명시되어 있어서 무조건 파이썬 소켓을 이용한 시스템 해킹(원격 익스플로잇) 방식으로 공격을 감행해야 하는 줄 알고 스크립트를 조율하며 긴 시간 삽질을 유발했다.</li>
<li><strong>새로 알게 된 점:</strong> 문제의 본질은 원격 타격이 아니라 &quot;도커 환경을 로컬에서 다룰 수 있는가&quot;에 대한 개발 및 인프라 기본기 검증이었다. 무작정 툴부터 켜기 전에 문제 지문과 요구사항을 냉정하고 명확하게 파악하는 안목이 가장 중요하다는 것을 깨달았다.</li>
<li><strong>보안 대책 기여:</strong> 도커 컨테이너 내부 셸을 탈취하는 <code>docker exec -it</code> 명령어는 개발 및 디버깅 시 매우 강력하지만, 프로덕션 환경에서 아무에게나 이 제어 권한이 노출될 경우 컨테이너에 격리된 모든 중요 설정 파일과 크레덴셜 정보(<code>flag</code>)가 한순간에 탈취당할 수 있다. 따라서 실제 운영 환경에서는 컨테이너 내부 접근 권한을 엄격히 제한하고 롤 기반 접근 제어(RBAC) 및 로깅 가시성을 확보해야 함을 복기했다.</li>
</ul>