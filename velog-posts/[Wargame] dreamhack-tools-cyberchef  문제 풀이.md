<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.31</li>
<li>문제명: dreamhack-tools-cyberchef</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/270">https://dreamhack.io/wargame/challenges/270</a></li>
<li>핵심 키워드: CyberChef, Base64, ROT13, Rail Fence Cipher, Data Encoding</li>
</ul>
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제공된 index.html 파일에 들어가 보면 다음과 같은 문자열과 힌트가 제공된다.</p>
<ul>
<li><p>Target 문자열: EUg5MJAyYJ9fYJ5iMKqio29iVK1VL2WlnTM0o3AyL2Elq3q3qlRu</p>
</li>
<li><p>힌트: Rail Fence → Base64 → ROT13</p>
</li>
</ul>
<p>해당 내용을 분석해 보면, 타겟 문자열은 플래그 원본을 Rail Fence → Base64 → ROT13 순서로 인코딩 및 암호화한 결과물이다.
그렇다면 원본 플래그를 얻기 위해서는 역순인 ROT13 → Base64 → Rail Fence Cipher 순서로 디코딩(Decoding)을 진행해야 한다.</p>
<ul>
<li>드림핵에서 제공하는 드림핵 툴즈 서비스 (<a href="https://tools.dreamhack.games/cyberchef">https://tools.dreamhack.games/cyberchef</a>) 사용</li>
</ul>
<hr />
<h2 id="3-문제-해결-과정-웹-실습">3. 문제 해결 과정 (웹 실습)</h2>
<p>다양한 인코딩/디코딩 기능을 제공하는 웹 툴인 CyberChef(사이버셰프)를 활용하여 역순으로 분석을 진행했다.</p>
<ol>
<li><p>ROT13 Decode:</p>
<p> 입력: EUg5MJAyYJ9fYJ5iMKqio29iVK1VL2WlnTM0o3AyL2Elq3q3qlRu</p>
<p> 출력(ROT13 디코딩 결과): (Base64로 인코딩되어 있는 중간 문자열 획득)</p>
</li>
<li><p>From Base64 (Base64 Decode):</p>
<p> 위에서 얻은 문자열을 다시 Base64로 디코딩한다.</p>
<p> 출력: (Rail Fence로 암호화된 중간 문자열 획득)</p>
</li>
<li><p>Rail Fence Cipher Decode:</p>
<p> 마지막으로 Rail Fence Cipher를 디코딩(Key/Depth 값 조정 필요)한다.</p>
<p> 최종 플래그 획득: DH{cyberchef-tools-encoderwwowowowo!!!}</p>
</li>
</ol>
<hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<table>
<thead>
<tr>
<th>기법(알고리즘)</th>
<th>동작 원리 및 특징</th>
<th>인프라/보안 관점</th>
</tr>
</thead>
<tbody><tr>
<td>ROT13</td>
<td>알파벳을 13글자씩 밀어서 치환하는 단순 카이사르 암호(Caesar cipher)의 일종이다. 영문 알파벳이 26자이므로 두 번 적용하면 원본으로 돌아온다.</td>
<td>암호학적 가치가 전혀 없는 단순 난독화(Obfuscation) 기법이다.</td>
</tr>
<tr>
<td>Base64</td>
<td>8비트 이진 데이터(Binary)를 문자 코드에 영향을 받지 않는 공통 ASCII 영역의 64개 문자(A-Z, a-z, 0-9, +, /)로 이루어진 문자열로 변환한다.</td>
<td>통신 시 데이터가 깨지는 것을 방지하기 위해 사용된다. 쿠버네티스(Kubernetes)의 Secret이나 HTTP Basic Auth 등 인프라 전반에서 광범위하게 쓰인다.</td>
</tr>
<tr>
<td>Rail Fence Cipher</td>
<td>문자열을 지그재그(울타리 모양)로 쓰고, 이를 가로줄 순서대로 다시 읽어내는 전치 암호(Transposition cipher)다.</td>
<td>고전 암호 방식 중 하나로, 텍스트의 배열 위치만 바꾸기 때문에 키(Depth)만 찾으면 쉽게 풀린다.</td>
</tr>
</tbody></table>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>인코딩(Encoding)과 암호화(Encryption)의 철저한 구분:</strong> 이번 문제를 풀면서 Base64나 ROT13 같은 기법은 '암호화'가 아니라 단순히 데이터를 다른 포맷으로 변환하는 '인코딩/난독화'에 불과하다는 것을 다시 한번 깨달았다. 실제 인프라 환경(예: Kubernetes Secret)에서도 중요 데이터를 Base64로 저장하는 경우가 많은데, 이는 누구나 쉽게 디코딩할 수 있으므로 절대 보안 조치라고 착각해서는 안 된다. 민감한 데이터는 반드시 AWS KMS나 HashiCorp Vault 같은 정식 암호화(Encryption) 솔루션을 통해 관리해야 함을 명심하게 되었다.</li>
<li><strong>보안 엔지니어의 만능 도구, CyberChef:</strong> 복잡하게 꼬여있는 로그 데이터나 WAF(웹 방화벽)에서 탐지된 알 수 없는 페이로드를 분석할 때, CyberChef 하나로 파이프라인을 구축해 순식간에 원본을 복원해 낼 수 있다는 것을 배웠다. 앞으로 실무에서 악성 스크립트나 인젝션 페이로드를 마주칠 때, 이 툴을 적극적으로 활용하여 빠르고 정확하게 분석할 수 있을 것 같다.</li>
</ul>