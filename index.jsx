import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to Harit Vatika Project pvt.ltd
        </h1>

        <p className={styles.description}>
          Residential plots near jewar international Airport
        </p>

        <div className={styles.grid}>
          <Link href="/budget" className={styles.card}>
            <h3> Plot size according to your budget &rarr;</h3>
          </Link>

          <Link href="/size" className={styles.card}>
            <h3>Residential plots sizes &rarr;</h3>
          </Link>

          <Link href="/facilities" className={styles.card}>
            <h3>Facilities and Amenities of society &rarr;</h3>
          </Link>

          <Link
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
          >
            <h3>prices of residential plot &rarr;</h3>
            <p></p>
          </Link>

          <Link
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
          >
            <h3>plocation of site &rarr;</h3>
            <p></p>
          </Link>
        </div>
      </main>

      <footer className={styles.footer}>
        Created using&nbsp;<b>next.new</b>&nbsp;⚡️
      </footer>
    </div>
  );
}
