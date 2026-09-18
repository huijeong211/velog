<h2 id="1-학습-개요">1. 학습 개요</h2>
<ul>
<li><strong>학습일:</strong> 2026.09.17</li>
<li><strong>교육명:</strong> AWS Cloud Essentials - Knowledge Badge Readiness Path (includes Labs)</li>
<li><strong>모듈명</strong>: Module 1. Job Roles in the Cloud</li>
<li><strong>핵심 키워드:</strong> 온프레미스(On-premises), 클라우드 직무 전환, 공동 책임 모델(Shared Responsibility Model), Cloud Architect, DevOps Administrator</li>
</ul>
<h2 id="2-학습-목표-및-분석">2. 학습 목표 및 분석</h2>
<p>본격적인 AWS 인프라 구축과 서비스(EC2, S3 등) 학습에 앞서, '클라우드 환경에서 인프라 엔지니어의 역할이 어떻게 변화하는가?'를 짚어보는 챕터이다.
과거 온프레미스 환경에서는 하드웨어 고장, 서버실 온도(HVAC), 물리적 장비 조립 및 패치 등 물리적인 유지 보수에 막대한 리소스가 소모되었다. 하지만 AWS 클라우드로 전환되면서 이러한 물리적 작업의 상당 부분을 AWS가 대신 처리하게 된다. 이를 통해 엔지니어는 단순 유지 보수를 넘어 아키텍처 설계와 최적화 혁신에 집중할 수 있는 환경으로 진화한다. 이 모듈에서는 전통적인 온프레미스 직무가 클라우드에서 어떻게 매핑되고 확장되는지 분석한다.</p>
<h2 id="3-핵심-개념-요약">3. 핵심 개념 요약</h2>
<p>클라우드 직무를 논하기 전, 모든 인프라 설계의 대전제는 공동 책임 모델(Shared Responsibility Model)이다.</p>
<ul>
<li><strong>AWS의 책임 (Security OF the Cloud):</strong> 데이터 센터 물리적 시설, 서버 하드웨어, 네트워크 인프라 보호 등 클라우드 자체의 보안을 전적으로 책임진다.</li>
</ul>
<p><strong>고객(엔지니어)의 책임 (Security IN the Cloud):</strong> OS 패치, 데이터 보호, 방화벽(Security Group) 설정, IAM 권한 관리를 책임진다. 이 영역은 보안 및 시스템 운영 엔지니어의 핵심 임무가 된다.</p>
<h2 id="4-인프라-직무-역할-매핑-분석-on-premises-→-cloud">4. 인프라 직무 역할 매핑 분석 (On-premises → Cloud)</h2>
<p>온프레미스의 물리적 요소들이 클라우드 환경에서 어떻게 논리적인 직무로 1:1 매핑되는지 표로 정리했다.</p>
<table>
<thead>
<tr>
<th>온프레미스 직무 역할</th>
<th>클라우드 매핑 및 진화된 직무 (AWS)</th>
<th>인프라 엔지니어 관점의 역할 변화</th>
</tr>
</thead>
<tbody><tr>
<td>데이터베이스 관리자 (DBA)</td>
<td>클라우드 아키텍트 (Cloud Architect) 등으로 수평 이동</td>
<td>하드웨어 패치나 조달 업무에서 벗어나, 고가용성·비용 효율성·확장성을 갖춘 데이터베이스 및 인프라 청사진을 설계한다.</td>
</tr>
<tr>
<td>시스템 관리자 (SysAdmin)</td>
<td>AWS SysOps / 클라우드 운영 엔지니어</td>
<td>서버실 장비 관리 대신, 하이브리드 및 클라우드 솔루션을 배포·구성·모니터링하며 데이터 무결성을 유지하고 팀을 감독한다.</td>
</tr>
<tr>
<td>네트워크 / 보안 관리자</td>
<td>AWS Security Administrator</td>
<td>공동 책임 모델에 따라 데이터와 리소스의 무결성·기밀성을 책임진다. 사고 발생 후 대응하는 '반응적' 역할과 표준을 수립해 사고를 줄이는 '선제적' 역할을 동시에 수행한다.</td>
</tr>
<tr>
<td>애플리케이션 / 기타 관리자</td>
<td>DevOps Administrator</td>
<td>빌드, 통합, 배포(CI/CD) 및 코드형 인프라(IaC)를 구현한다. 타 팀에 의존하는 정도가 줄어들고, 프로그래밍 스크립팅을 통해 테스트와 롤백 주기를 조율하여 빠른 릴리스를 지원한다.</td>
</tr>
<tr>
<td>## 5. 배운 점 및 회고</td>
<td></td>
<td></td>
</tr>
</tbody></table>
<p><strong>물리적 유지보수에서 논리적 최적화로의 시선 전환:</strong> 온프레미스 환경에서는 서버실 온도나 하드웨어 패치 같은 궂은일에 많은 시간을 쏟아야 했지만, 클라우드에서는 AWS가 이 밑바닥을 지켜주기 때문에 엔지니어가 비즈니스 혁신과 아키텍처 최적화에 집중할 수 있다는 점이 매우 인상 깊었다. 코드로 인프라를 통제해야 하는 만큼, 꾸준히 파이썬 등 코딩 기초를 다져온 것이 향후 DevOps나 자동화 파이프라인을 다룰 때 강력한 무기가 될 것이다.</p>
<p><strong>명확해진 엔지니어의 책임 범위 (Security &amp; DevOps):</strong> 안 관리자(Security Administrator)가 단순 사고 대응을 넘어 선제적인 표준 프로세스를 수립해야 하듯, 클라우드 인프라를 다룰 때는 '최소 권한의 원칙'과 철저한 통제가 필수적임을 느꼈다. 드림핵 워게임을 풀며 익혔던 웹 취약점 및 방어 로직 관점을 클라우드 아키텍처 설계에 녹여내어, 탄탄한 보안 마인드를 가진 'DevSecOps 엔지니어'로 성장할 것 이다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/58ec3118-4eda-49e5-857a-b584529af060/image.png" /></p>